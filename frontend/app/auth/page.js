'use client'
import { useState } from 'react'
import { useRouter } from 'next/navigation'
import Header from '../components/Header'
import { authAPI } from '../lib/api'
import Link from 'next/link'

export default function LoginPage() {
  const router = useRouter()
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  })
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)

    try {
      const response = await authAPI.login(formData)
      localStorage.setItem('token', response.data.token)
      localStorage.setItem('user', JSON.stringify(response.data.user))
      router.push('/account')
    } catch (err) {
      setError(err.response?.data?.error || 'Login failed')
      setLoading(false)
    }
  }

  return (
    <>
      <Header />
      <main className="auth-shell">
        <section className="auth-card">
          <p className="eyebrow">Welcome back</p>
          <h1>Login</h1>

        {error && (
          <div className="notice error">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="stack">
          <div>
            <label>Username</label>
            <input
              type="text"
              name="username"
              value={formData.username}
              onChange={handleChange}
              required
            />
          </div>

          <div>
            <label>Password</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="button full-width"
          >
            {loading ? 'Logging in...' : 'Login'}
          </button>
        </form>

        <p className="form-footer">
          Don't have an account?{' '}
          <Link href="/auth/signup">
            Sign up
          </Link>
        </p>
        </section>
      </main>
    </>
  )
}
