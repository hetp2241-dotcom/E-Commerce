'use client'
import { useState } from 'react'
import Header from '../components/Header'
import { ordersAPI, paymentsAPI } from '../lib/api'
import { useRouter } from 'next/navigation'

export default function CheckoutPage() {
  const router = useRouter()
  const [formData, setFormData] = useState({
    shipping_address: '',
    billing_address: '',
    shipping_cost: 10,
    tax: 0,
    discount: 0,
    coupon_code: '',
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({
      ...prev,
      [name]: name === 'shipping_cost' ? parseFloat(value) : value,
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)

    try {
      // Create order
      const orderResponse = await ordersAPI.create(formData)
      const order = orderResponse.data.order

      // Process payment
      await paymentsAPI.process({
        order_id: order.id,
        payment_method: 'stripe',
      })

      // Redirect to order confirmation
      router.push(`/account/orders/${order.id}`)
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to process checkout')
      setLoading(false)
    }
  }

  return (
    <>
      <Header />
      <main className="container narrow">
        <div className="page-heading">
          <p className="eyebrow">Secure Checkout</p>
          <h1>Checkout</h1>
          <p>Confirm shipping, billing, and payment details to place your order.</p>
        </div>

        {error && (
          <div className="notice error">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="stack">
          <section className="panel">
            <h2>Shipping Address</h2>
            <textarea
              name="shipping_address"
              value={formData.shipping_address}
              onChange={handleChange}
              placeholder="Enter your shipping address"
              rows="4"
              required
            />
          </section>

          <section className="panel">
            <h2>Billing Address</h2>
            <label className="check-row">
              <input
                type="checkbox"
                onChange={(e) => {
                  if (e.target.checked) {
                    setFormData((prev) => ({
                      ...prev,
                      billing_address: prev.shipping_address,
                    }))
                  }
                }}
              />
              <span>Same as shipping address</span>
            </label>
            <textarea
              name="billing_address"
              value={formData.billing_address}
              onChange={handleChange}
              placeholder="Enter your billing address"
              rows="4"
            />
          </section>

          <section className="panel">
            <h2>Promo Code</h2>
            <input
              type="text"
              name="coupon_code"
              value={formData.coupon_code}
              onChange={handleChange}
              placeholder="Enter coupon code (optional)"
            />
          </section>

          <section className="panel summary-panel">
            <h2>Order Summary</h2>
            <div className="summary-lines">
              <div>
                <span>Shipping Cost:</span>
                <span>${formData.shipping_cost}</span>
              </div>
              <div>
                <span>Tax:</span>
                <span>${formData.tax}</span>
              </div>
              {formData.discount > 0 && (
                <div>
                  <span>Discount:</span>
                  <span>-${formData.discount}</span>
                </div>
              )}
            </div>
          </section>

          <button
            type="submit"
            disabled={loading}
            className="button full-width"
          >
            {loading ? 'Processing...' : 'Complete Purchase'}
          </button>
        </form>
      </main>
    </>
  )
}
