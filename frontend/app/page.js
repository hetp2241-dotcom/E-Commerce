import Link from 'next/link'
import Header from './components/Header'

export default function Home() {
  return (
    <>
      <Header />
      <main>
        <section className="hero">
          <div className="container hero-grid">
            <div className="hero-copy">
              <p className="eyebrow">Curated essentials, fast checkout</p>
              <h1>ShopSphere</h1>
              <p>
                Discover thoughtful tech, lifestyle, and home products with clean browsing,
                live inventory, secure checkout, and order tracking in one place.
              </p>
              <div className="hero-actions">
                <Link href="/products" className="button">Shop products</Link>
                <Link href="/auth/signup" className="ghost-button">Create account</Link>
              </div>
            </div>
            <div className="hero-panel" aria-label="Featured categories">
              <div className="showcase-tile large">Audio</div>
              <div className="showcase-tile">Wearables</div>
              <div className="showcase-tile accent">Home</div>
            </div>
          </div>
        </section>

        <section className="container section-grid">
          <div>
            <p className="eyebrow">Why shoppers come back</p>
            <h2>Everything needed for a modern storefront.</h2>
          </div>
          <div className="feature-grid">
            <div className="feature"><strong>Fresh catalog</strong><span>Browse by category, search, and price-sort in seconds.</span></div>
            <div className="feature"><strong>Customer cart</strong><span>Authenticated carts keep quantities and totals consistent.</span></div>
            <div className="feature"><strong>Order history</strong><span>Customers can review paid orders from their account dashboard.</span></div>
          </div>
        </section>
      </main>
    </>
  )
}
