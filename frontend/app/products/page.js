'use client'
import { useEffect, useState } from 'react'
import Header from '../components/Header'
import ProductCard from '../components/ProductCard'
import { cartAPI, productsAPI, unwrapList } from '../lib/api'
import Link from 'next/link'

export default function ProductsPage() {
  const [products, setProducts] = useState([])
  const [categories, setCategories] = useState([])
  const [loading, setLoading] = useState(true)
  const [selectedCategory, setSelectedCategory] = useState('')
  const [search, setSearch] = useState('')
  const [ordering, setOrdering] = useState('-created_at')
  const [notice, setNotice] = useState('')
  const [isSignedIn, setIsSignedIn] = useState(false)

  useEffect(() => {
    fetchProducts()
  }, [selectedCategory, ordering])

  useEffect(() => {
    fetchCategories()
    setIsSignedIn(Boolean(localStorage.getItem('token')))
  }, [])

  const fetchProducts = async () => {
    try {
      setLoading(true)
      const response = await productsAPI.list({
        category: selectedCategory || undefined,
        search: search || undefined,
        ordering,
      })
      setProducts(unwrapList(response.data))
    } catch (error) {
      console.error('Error fetching products:', error)
    } finally {
      setLoading(false)
    }
  }

  const fetchCategories = async () => {
    try {
      const response = await productsAPI.categories()
      setCategories(unwrapList(response.data))
    } catch (error) {
      console.error('Error fetching categories:', error)
    }
  }

  const addToCart = async (product) => {
    if (!localStorage.getItem('token')) {
      setNotice('Sign in to add products to your cart.')
      setIsSignedIn(false)
      return
    }

    try {
      await cartAPI.addItem({ product_id: product.id, quantity: 1 })
      setNotice(`${product.name} added to your cart.`)
    } catch (error) {
      setNotice(error.response?.data?.error || 'Could not add this product to your cart.')
    }
  }

  return (
    <>
      <Header />
      <main className="container">
        <div className="page-heading">
          <p className="eyebrow">Catalog</p>
          <h1>Products</h1>
          <p>Search the catalog, filter by category, and add items to your cart.</p>
        </div>

        <form className="toolbar" onSubmit={(event) => { event.preventDefault(); fetchProducts() }}>
          <input
            value={search}
            onChange={(event) => setSearch(event.target.value)}
            placeholder="Search products"
            aria-label="Search products"
          />
          <select value={selectedCategory} onChange={(event) => setSelectedCategory(event.target.value)} aria-label="Category">
            <option value="">All categories</option>
            {categories.map((category) => (
              <option key={category.id} value={category.id}>{category.name}</option>
            ))}
          </select>
          <select value={ordering} onChange={(event) => setOrdering(event.target.value)} aria-label="Sort products">
            <option value="-created_at">Newest</option>
            <option value="base_price">Price low to high</option>
            <option value="-base_price">Price high to low</option>
          </select>
          <button className="button" type="submit">Search</button>
        </form>

        {notice && (
          <div className="notice">
            <span>{notice}</span>
            {!isSignedIn && <Link href="/auth">Sign in</Link>}
          </div>
        )}

        {loading ? (
          <div className="empty-state">Loading products...</div>
        ) : products.length === 0 ? (
          <div className="empty-state">No products found. Add products in Django admin or change your filters.</div>
        ) : (
          <div className="product-grid">
            {products.map((product) => (
              <ProductCard key={product.id} product={product} onAdd={addToCart} />
            ))}
          </div>
        )}
      </main>
    </>
  )
}
