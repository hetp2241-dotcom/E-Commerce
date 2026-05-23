import Link from 'next/link'
import Header from '../components/Header'

export default function AdminShortcutPage() {
  return (
    <>
      <Header />
      <main className="container narrow">
        <section className="panel center-panel">
          <p className="eyebrow">Store operations</p>
          <h1>Admin Console</h1>
          <p>Manage catalog, orders, shipping methods, payments, reviews, and support tickets from Django admin.</p>
          <a href="http://localhost:8002/admin/" className="button">Open Django admin</a>
          <Link href="/products" className="ghost-button">Back to storefront</Link>
        </section>
      </main>
    </>
  )
}
