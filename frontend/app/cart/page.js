'use client'
import { useEffect, useState } from 'react'
import Header from '../components/Header'
import { cartAPI } from '../lib/api'
import Link from 'next/link'

export default function CartPage() {
  const [cart, setCart] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchCart()
  }, [])

  const fetchCart = async () => {
    try {
      const response = await cartAPI.get()
      setCart(response.data)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching cart:', error)
      setLoading(false)
    }
  }

  const removeItem = async (itemId) => {
    try {
      const response = await cartAPI.removeItem({ item_id: itemId })
      setCart(response.data)
    } catch (error) {
      console.error('Error removing item:', error)
    }
  }

  const updateQuantity = async (itemId, quantity) => {
    if (quantity === 0) {
      removeItem(itemId)
      return
    }
    try {
      const response = await cartAPI.updateItem({ item_id: itemId, quantity })
      setCart(response.data)
    } catch (error) {
      console.error('Error updating item:', error)
    }
  }

  if (loading) return <div>Loading...</div>

  return (
    <>
      <Header />
      <main className="container">
        <div className="page-heading">
          <p className="eyebrow">Cart</p>
          <h1>Shopping Cart</h1>
        </div>

        {!cart || cart.items.length === 0 ? (
          <div className="empty-state">
            <p>Your cart is empty.</p>
            <Link href="/products" className="button">
              Continue Shopping
            </Link>
          </div>
        ) : (
          <div className="checkout-grid">
            <section className="panel">
              <div className="stack">
                {cart.items.map((item) => (
                  <div
                    key={item.id}
                    className="cart-line"
                  >
                    <div>
                      <h3>{item.product.name}</h3>
                      <p>${item.product.current_price}</p>
                    </div>
                    <div className="line-actions">
                      <input
                        type="number"
                        min="1"
                        value={item.quantity}
                        onChange={(e) =>
                          updateQuantity(item.id, parseInt(e.target.value))
                        }
                      />
                      <strong>${item.total}</strong>
                      <button
                        onClick={() => removeItem(item.id)}
                        className="ghost-button compact danger"
                      >
                        Remove
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </section>

            <aside className="panel summary-panel">
              <h2>Order Summary</h2>
              <div className="summary-lines">
                <div>
                  <span>Subtotal:</span>
                  <span>${cart.total_price}</span>
                </div>
                <div>
                  <span>Shipping:</span>
                  <span>TBD</span>
                </div>
                <div>
                  <span>Tax:</span>
                  <span>TBD</span>
                </div>
              </div>
              <div className="summary-total">
                <span>Total:</span>
                <span>${cart.total_price}</span>
              </div>
              <Link
                href="/checkout"
                className="button full-width"
              >
                Proceed to Checkout
              </Link>
            </aside>
          </div>
        )}
      </main>
    </>
  )
}
