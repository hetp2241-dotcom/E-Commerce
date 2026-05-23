import Link from 'next/link'

const money = (value) => `$${Number(value || 0).toFixed(2)}`

export default function ProductCard({ product, onAdd }) {
  const primaryImage = product.images?.find((image) => image.is_primary) || product.images?.[0]

  return (
    <article className="product-card">
      <Link href={`/products/${product.slug}`} className="product-media" aria-label={product.name}>
        {primaryImage?.image ? (
          <img src={primaryImage.image} alt={primaryImage.alt_text || product.name} />
        ) : (
          <span>{product.category_name || product.category?.name || 'Product'}</span>
        )}
      </Link>
      <div className="product-card-body">
        <div>
          <p className="eyebrow">{product.category_name || product.category?.name || 'Featured'}</p>
          <Link href={`/products/${product.slug}`} className="product-title">
            {product.name}
          </Link>
        </div>
        <div className="price-row">
          <span>{money(product.current_price)}</span>
          {product.discount_price && <del>{money(product.base_price)}</del>}
        </div>
        <p className={product.stock > 0 ? 'stock in-stock' : 'stock out-stock'}>
          {product.stock > 0 ? `${product.stock} in stock` : 'Out of stock'}
        </p>
        <button className="button full-width" disabled={!product.stock} onClick={() => onAdd?.(product)}>
          Add to Cart
        </button>
      </div>
    </article>
  )
}
