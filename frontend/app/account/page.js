'use client'
import { useEffect, useState } from 'react'
import Link from 'next/link'
import Header from '../components/Header'
import { authAPI, ordersAPI, unwrapList } from '../lib/api'

const money = (value) => `$${Number(value || 0).toFixed(2)}`

export default function AccountPage() {
  const [profile, setProfile] = useState(null)
  const [orders, setOrders] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [isSignedIn, setIsSignedIn] = useState(false)

  useEffect(() => {
    const loadAccount = async () => {
      if (!localStorage.getItem('token')) {
        setLoading(false)
        return
      }

      setIsSignedIn(true)

      try {
        const [profileResponse, ordersResponse] = await Promise.all([
          authAPI.getProfile(),
          ordersAPI.list(),
        ])
        setProfile(profileResponse.data)
        setOrders(unwrapList(ordersResponse.data))
      } catch (err) {
        setError('We could not load your account right now.')
      } finally {
        setLoading(false)
      }
    }

    loadAccount()
  }, [])

  return (
    <>
      <Header />
      <main className="container">
        <div className="page-heading">
          <p className="eyebrow">Account</p>
          <h1>Your dashboard</h1>
        </div>

        {loading ? (
          <div className="empty-state">Loading account...</div>
        ) : !isSignedIn ? (
          <div className="empty-state">
            <p>Sign in to view your profile, cart, and orders.</p>
            <Link href="/auth" className="button">Sign in</Link>
          </div>
        ) : (
          <div className="account-grid">
            <section className="panel">
              <h2>Profile</h2>
              {error && <div className="notice error">{error}</div>}
              <div className="detail-list">
                <div><span>Name</span><strong>{profile?.user?.first_name || profile?.user?.username || 'Customer'}</strong></div>
                <div><span>Email</span><strong>{profile?.user?.email || 'Not added'}</strong></div>
                <div><span>Phone</span><strong>{profile?.phone || 'Not added'}</strong></div>
              </div>
            </section>

            <section className="panel">
              <h2>Recent orders</h2>
              {orders.length === 0 ? (
                <p className="muted">No orders yet. Your completed purchases will appear here.</p>
              ) : (
                <div className="stack">
                  {orders.map((order) => (
                    <div className="order-row" key={order.id}>
                      <div>
                        <strong>{order.order_number}</strong>
                        <span>{order.status}</span>
                      </div>
                      <strong>{money(order.total)}</strong>
                    </div>
                  ))}
                </div>
              )}
            </section>
          </div>
        )}
      </main>
    </>
  )
}
