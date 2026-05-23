'use client'
import Link from 'next/link'
import { useEffect, useState } from 'react'

export default function Header() {
  const [user, setUser] = useState(null)

  useEffect(() => {
    const stored = localStorage.getItem('user')
    setUser(stored ? JSON.parse(stored) : null)
  }, [])

  const logout = () => {
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    setUser(null)
    window.location.href = '/'
  }

  return (
    <header className="site-header">
      <div className="container nav-shell">
        <Link href="/" className="brand">
          <span className="brand-mark">S</span>
          <span>ShopSphere</span>
        </Link>
        <nav className="nav-links" aria-label="Primary navigation">
          <Link href="/">Home</Link>
          <Link href="/products">Products</Link>
          <Link href="/cart">Cart</Link>
          <Link href="/account">Account</Link>
        </nav>
        <div className="nav-actions">
          {user ? (
            <button className="ghost-button compact" onClick={logout}>
              Logout
            </button>
          ) : (
            <Link href="/auth" className="button compact">
              Sign in
            </Link>
          )}
        </div>
      </div>
    </header>
  )
}
