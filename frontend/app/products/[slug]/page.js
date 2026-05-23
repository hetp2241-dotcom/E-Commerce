'use client'
import { useEffect, useState } from 'react'
import Link from 'next/link'
import Header from '../../components/Header'
import { cartAPI, productsAPI } from '../../lib/api'

const money = (value) => `$${Number(value || 0).toFixed(2)}`

export default function ProductDetailPage({ params }) {
  const [product, setProduct] = useState(null)
  const [loading, setLoading] = useState(true)
  const [quantity, setQuantity] = useState(1)
  const [notice, setNotice] = useState('')

  useEffect(() => {
    const loadProduct = async () => {
      try {
        const response = await productsAPI.detail(params.slug)
        setProduct(response.data)
      } catch (error) {
        setNotice('This product could not be loaded.')
      } finally {
        setLoading(false)
      }
    }

    loadProduct()
  }, [params.slug])

  const addToCart = async () => {
    if (!localStorage.getItem('token')) {
      setNotice('Sign in to add this item to your cart.')
      return
    }

    try {
      await cartAPI.addItem({ product_id: product.id, quantity })
      setNotice(`${product.name} added to your cart.`)
    } catch (error) {
      setNotice(error.response?.data?.error || 'Could not add this item to your cart.')
    }
  }

  const image = product?.images?.find((item) => item.is_primary) || product?.images?.[0]

  return (
    <>
      <Header />
      <main className="container">
        {loading ? (
          <div className="empty-state">Loading product...</div>
        ) : !product ? (
          <div className="empty-state">
            <p>Product not found.</p>
            <Link href="/products" className="button">Back to products</Link>
          </div>
        ) : (
          <section className="product-detail">
            <div className="detail-media">
              {image?.image ? <img src={image.image} alt={image.alt_text || product.name} /> : <span>{product.category?.name}</span>}
            </div>
            <div className="detail-copy">
              <p className="eyebrow">{product.category?.name || 'Product'}</p>
              <h1>{product.name}</h1>
              <div className="price-row detail-price">
                <span>{money(product.current_price)}</span>
                {product.discount_price && <del>{money(product.base_price)}</del>}
              </div>
              <p>{product.description}</p>
              <p className={product.stock > 0 ? 'stock in-stock' : 'stock out-stock'}>
                {product.stock > 0 ? `${product.stock} available` : 'Out of stock'}
              </p>
              {notice && <div className="notice">{notice}</div>}
              <div className="purchase-row">
                <input
                  type="number"
                  min="1"
                  max={product.stock || 1}
                  value={quantity}
                  onChange={(event) => setQuantity(Number(event.target.value))}
                  aria-label="Quantity"
                />
                <button className="button" disabled={!product.stock} onClick={addToCart}>
                  Add to Cart
                </button>
              </div>
              {product.variants?.length > 0 && (
                <div className="panel subtle-panel">
                  <h2>Available options</h2>
                  <div className="chip-row">
                    {product.variants.map((variant) => (
                      <span className="chip" key={variant.id}>{variant.name}</span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </section>
        )}
      </main>
    </>
  )
}
