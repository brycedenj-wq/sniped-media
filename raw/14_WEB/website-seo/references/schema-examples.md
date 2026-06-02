# Schema Markup Examples

Complete JSON-LD examples for common schema types. Copy, customize, and paste into your pages.

---

## Contents
- [Organization](#organization)
- [WebSite (with SearchAction)](#website-with-searchaction)
- [Article / BlogPosting](#article--blogposting)
- [Product](#product)
- [SoftwareApplication](#softwareapplication)
- [FAQPage](#faqpage)
- [HowTo](#howto)
- [BreadcrumbList](#breadcrumblist)
- [LocalBusiness](#localbusiness)
- [Event](#event)
- [Multiple Schema Types (@graph)](#multiple-schema-types-graph)
- [Implementation Example (Next.js)](#implementation-example-nextjs)

---

## Organization

For company/brand homepage or about page.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Example Company",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": [
    "https://twitter.com/example",
    "https://linkedin.com/company/example",
    "https://facebook.com/example"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-555-555-5555",
    "contactType": "customer service"
  }
}
```

**Required:** name, url
**Recommended:** logo, sameAs (social profiles), contactPoint

---

## WebSite (with SearchAction)

For homepage. Enables sitelinks search box in Google results.

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Example",
  "url": "https://example.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

**Required:** name, url
**Recommended:** potentialAction (SearchAction)

---

## Article / BlogPosting

For blog posts and news articles. Use `BlogPosting` for blog content, `Article` for general articles, `NewsArticle` for news.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Implement Schema Markup",
  "image": "https://example.com/image.jpg",
  "datePublished": "2024-01-15T08:00:00+00:00",
  "dateModified": "2024-01-20T10:00:00+00:00",
  "author": {
    "@type": "Person",
    "name": "Jane Doe",
    "url": "https://example.com/authors/jane"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Example Company",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "description": "A complete guide to implementing schema markup for better search visibility and rich results.",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/schema-guide"
  }
}
```

**Required:** headline, image, datePublished, author
**Recommended:** dateModified, publisher, description, mainEntityOfPage

---

## Product

For product pages (e-commerce or SaaS).

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Premium Widget",
  "image": "https://example.com/widget.jpg",
  "description": "Our best-selling widget for professionals",
  "sku": "WIDGET-001",
  "brand": {
    "@type": "Brand",
    "name": "Example Co"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/products/widget",
    "priceCurrency": "USD",
    "price": "99.99",
    "availability": "https://schema.org/InStock",
    "priceValidUntil": "2024-12-31"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "127"
  }
}
```

**Required:** name, image, offers (with price and availability)
**Recommended:** sku, brand, aggregateRating, review, description

---

## SoftwareApplication

For SaaS product pages and app landing pages.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Example App",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web, iOS, Android",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.6",
    "ratingCount": "1250"
  }
}
```

**Required:** name, offers
**Recommended:** applicationCategory, operatingSystem, aggregateRating

---

## FAQPage

For pages with frequently asked questions. Enables FAQ rich results in Google.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is schema markup?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Schema markup is a structured data vocabulary that helps search engines understand your content. It uses a standardized format (JSON-LD recommended) to describe entities, properties, and relationships on your page. When implemented correctly, it can enable rich results like FAQ dropdowns, star ratings, and recipe cards in search results."
      }
    },
    {
      "@type": "Question",
      "name": "How do I implement schema markup?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The recommended approach is to use JSON-LD format, placing the script in your page's head or at the end of the body. Create a script tag with type='application/ld+json', then add your structured data as a JSON object inside it. Test with Google's Rich Results Test before deploying."
      }
    },
    {
      "@type": "Question",
      "name": "Does schema markup help with SEO?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Schema markup does not directly impact rankings, but it enables rich results that significantly improve click-through rates. Pages with rich results can see 20-30% higher CTR. Additionally, schema markup helps AI search engines understand and cite your content, providing a 30-40% AI visibility boost."
      }
    }
  ]
}
```

**Required:** mainEntity (array of Question/Answer pairs)

---

## HowTo

For instructional content and tutorials. Enables step-by-step rich results.

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Add Schema Markup to Your Website",
  "description": "A step-by-step guide to implementing JSON-LD schema markup for better search visibility.",
  "totalTime": "PT15M",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Choose your schema type",
      "text": "Identify the appropriate schema type for your page content. Use Organization for your homepage, Article for blog posts, Product for product pages, and FAQPage for FAQ content.",
      "url": "https://example.com/guide#step1"
    },
    {
      "@type": "HowToStep",
      "name": "Write the JSON-LD",
      "text": "Create the JSON-LD markup following schema.org specifications. Include all required properties and as many recommended properties as possible for your chosen schema type.",
      "url": "https://example.com/guide#step2"
    },
    {
      "@type": "HowToStep",
      "name": "Add to your page",
      "text": "Insert the script tag with type='application/ld+json' in your page's head section or at the end of the body. The JSON-LD should be placed inside this script tag.",
      "url": "https://example.com/guide#step3"
    },
    {
      "@type": "HowToStep",
      "name": "Test and validate",
      "text": "Use Google's Rich Results Test to validate your markup. Fix any errors or warnings before deploying to production. Also check the Schema.org Validator for additional validation.",
      "url": "https://example.com/guide#step4"
    }
  ]
}
```

**Required:** name, step (array of HowToStep)
**Recommended:** description, totalTime, image

---

## BreadcrumbList

For any page with breadcrumb navigation.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "https://example.com/blog"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "SEO Guide",
      "item": "https://example.com/blog/seo-guide"
    }
  ]
}
```

**Required:** itemListElement (array with position, name, item)

---

## LocalBusiness

For local business location pages.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Example Coffee Shop",
  "image": "https://example.com/shop.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main Street",
    "addressLocality": "San Francisco",
    "addressRegion": "CA",
    "postalCode": "94102",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "37.7749",
    "longitude": "-122.4194"
  },
  "telephone": "+1-555-555-5555",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "08:00",
      "closes": "18:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Saturday"],
      "opens": "09:00",
      "closes": "15:00"
    }
  ],
  "priceRange": "$$"
}
```

**Required:** name, address
**Recommended:** geo, telephone, openingHoursSpecification, priceRange, image

---

## Event

For event pages, webinars, conferences.

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Annual Marketing Conference",
  "startDate": "2024-06-15T09:00:00-07:00",
  "endDate": "2024-06-15T17:00:00-07:00",
  "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {
    "@type": "VirtualLocation",
    "url": "https://example.com/conference"
  },
  "image": "https://example.com/conference.jpg",
  "description": "Join us for our annual marketing conference featuring industry leaders discussing the latest trends in digital marketing, AI, and growth strategy.",
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/conference/tickets",
    "price": "199",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "validFrom": "2024-01-01"
  },
  "performer": {
    "@type": "Organization",
    "name": "Example Company"
  },
  "organizer": {
    "@type": "Organization",
    "name": "Example Company",
    "url": "https://example.com"
  }
}
```

**Required:** name, startDate, location
**Recommended:** endDate, eventAttendanceMode, eventStatus, offers, image, description

---

## Multiple Schema Types (@graph)

Combine multiple schema types on one page using `@graph`. Use `@id` to create references between types.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Example Company",
      "url": "https://example.com",
      "logo": "https://example.com/logo.png",
      "sameAs": [
        "https://twitter.com/example",
        "https://linkedin.com/company/example"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "url": "https://example.com",
      "name": "Example",
      "publisher": {
        "@id": "https://example.com/#organization"
      },
      "potentialAction": {
        "@type": "SearchAction",
        "target": {
          "@type": "EntryPoint",
          "urlTemplate": "https://example.com/search?q={search_term_string}"
        },
        "query-input": "required name=search_term_string"
      }
    },
    {
      "@type": "WebPage",
      "@id": "https://example.com/blog/seo-guide/#webpage",
      "url": "https://example.com/blog/seo-guide",
      "name": "Complete SEO Guide",
      "isPartOf": {
        "@id": "https://example.com/#website"
      }
    },
    {
      "@type": "Article",
      "@id": "https://example.com/blog/seo-guide/#article",
      "headline": "Complete SEO Guide for 2024",
      "image": "https://example.com/seo-guide.jpg",
      "datePublished": "2024-01-15T08:00:00+00:00",
      "dateModified": "2024-03-01T10:00:00+00:00",
      "author": {
        "@type": "Person",
        "name": "Jane Doe",
        "url": "https://example.com/authors/jane"
      },
      "publisher": {
        "@id": "https://example.com/#organization"
      },
      "mainEntityOfPage": {
        "@id": "https://example.com/blog/seo-guide/#webpage"
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://example.com"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Blog",
          "item": "https://example.com/blog"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "SEO Guide",
          "item": "https://example.com/blog/seo-guide"
        }
      ]
    }
  ]
}
```

---

## Implementation Example (Next.js)

A reusable component for adding schema markup in Next.js applications.

### Pages Router (Next.js 12 and earlier)

```jsx
// components/SchemaMarkup.jsx
import Head from 'next/head';

export function SchemaMarkup({ schema }) {
  return (
    <Head>
      <script
        type="application/ld+json"
        // Use React's built-in HTML injection for JSON-LD
        // This is the standard pattern recommended by Next.js docs
        {...{ dangerouslySetInnerHTML: { __html: JSON.stringify(schema) } }}
      />
    </Head>
  );
}

// Usage in a product page
export default function ProductPage({ product }) {
  const schema = {
    "@context": "https://schema.org",
    "@type": "Product",
    name: product.name,
    image: product.image,
    description: product.description,
    sku: product.sku,
    brand: {
      "@type": "Brand",
      name: product.brand,
    },
    offers: {
      "@type": "Offer",
      url: `https://example.com/products/${product.slug}`,
      priceCurrency: "USD",
      price: product.price,
      availability: product.inStock
        ? "https://schema.org/InStock"
        : "https://schema.org/OutOfStock",
    },
    aggregateRating: product.rating
      ? {
          "@type": "AggregateRating",
          ratingValue: product.rating,
          reviewCount: product.reviewCount,
        }
      : undefined,
  };

  return (
    <>
      <SchemaMarkup schema={schema} />
      <h1>{product.name}</h1>
      <p>{product.description}</p>
    </>
  );
}
```

### App Router (Next.js 13+)

For Next.js App Router, render a `<script>` tag directly in the component:

```jsx
// app/blog/[slug]/page.jsx
export async function generateMetadata({ params }) {
  const post = await getPost(params.slug);
  return {
    title: post.title,
    description: post.excerpt,
  };
}

export default async function BlogPost({ params }) {
  const post = await getPost(params.slug);

  const schema = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: post.title,
    image: post.featuredImage,
    datePublished: post.publishedAt,
    dateModified: post.updatedAt,
    author: {
      "@type": "Person",
      name: post.author.name,
    },
  };

  return (
    <>
      <script
        type="application/ld+json"
        // Standard React pattern for injecting JSON-LD structured data
        {...{ dangerouslySetInnerHTML: { __html: JSON.stringify(schema) } }}
      />
      <article>
        <h1>{post.title}</h1>
      </article>
    </>
  );
}
```

### Homepage with Multiple Schema Types

```jsx
export default function HomePage() {
  const schema = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Organization",
        "@id": "https://example.com/#organization",
        name: "Example Company",
        url: "https://example.com",
        logo: "https://example.com/logo.png",
      },
      {
        "@type": "WebSite",
        "@id": "https://example.com/#website",
        url: "https://example.com",
        name: "Example",
        publisher: { "@id": "https://example.com/#organization" },
      },
    ],
  };

  return (
    <>
      <script
        type="application/ld+json"
        {...{ dangerouslySetInnerHTML: { __html: JSON.stringify(schema) } }}
      />
      <main>{/* Page content */}</main>
    </>
  );
}
```
