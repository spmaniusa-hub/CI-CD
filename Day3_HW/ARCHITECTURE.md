# Technical Architecture & Design System

This document outlines the architectural principles, component structure, design tokens, and technical implementation details of the **Mani Subramanian Executive Portfolio Webpage**.

---

## 🏛️ Architecture Overview

The portfolio is intentionally engineered as an **ultra-lightweight, zero-dependency static application** adhering to modern web development standards.

```
                    ┌─────────────────────────┐
                    │      index.html         │
                    │   (Semantic Layout)     │
                    └───────────┬─────────────┘
                                │
          ┌─────────────────────┴─────────────────────┐
          ▼                                           ▼
┌──────────────────┐                        ┌──────────────────┐
│    style.css     │                        │    script.js     │
│  - Design Tokens │                        │  - Theme Engine  │
│  - Dual Theme    │                        │  - Intersections │
│  - Glassmorphism │                        │  - Skills Filter │
│  - Responsive    │                        │  - Form & Clock  │
└──────────────────┘                        └──────────────────┘
```

### Core Design Philosophy
1. **Zero External Runtime Bloat**: No bulky JavaScript frameworks (React, Vue, Angular) or heavy CSS utilities (Tailwind bundle) are loaded at runtime.
2. **Instant Paint & Sub-100ms TTI**: Native browser DOM APIs ensure fast first contentful paint (FCP) and time-to-interactive (TTI).
3. **Executive Visual Hierarchy**: Glassmorphic panels, ambient gradient glow backdrops, and modern typography tailored for executive presentation.

---

## 🎨 Design System & CSS Tokens

All visual tokens are defined as CSS Custom Properties in `style.css`:

### 1. Dual Palette (Dark & Light)

| Token | Dark Mode (Default) | Light Mode | Purpose |
| :--- | :--- | :--- | :--- |
| `--bg-primary` | `#0a0f1d` | `#f8fafc` | Base background color |
| `--bg-secondary`| `#111827` | `#ffffff` | Elevated surface layers |
| `--bg-tertiary` | `#1a2236` | `#f1f5f9` | Inputs, pills, and secondary panels |
| `--bg-card` | `rgba(26, 34, 54, 0.65)` | `rgba(255, 255, 255, 0.9)` | Glassmorphic card surface |
| `--text-primary`| `#f8fafc` | `#0f172a` | High-contrast headers and primary text |
| `--text-secondary`| `#94a3b8` | `#475569` | Body copy and subtitles |
| `--border-color`| `rgba(255, 255, 255, 0.08)` | `rgba(15, 23, 42, 0.08)` | Subtle card borders |
| `--accent-gradient` | `linear-gradient(...)` | `linear-gradient(...)` | Electric Blue to Violet gradient |

### 2. Ambient Radial Lighting
Three fixed, blur-filtered radial gradient spheres create dynamic depth without SVG or heavy canvas overhead:
- `.glow-bg-1`: Blue primary ambient glow (`#3b82f6`) top-left.
- `.glow-bg-2`: Violet secondary ambient glow (`#8b5cf6`) middle-right.
- `.glow-bg-3`: Cyan subtle accent (`#06b6d4`) bottom-left.

### 3. Cross-Browser Typography & Gradient Clipping
To guarantee 100% compliance across Chromium, WebKit (Safari), and Gecko (Firefox) engines:
- **Dual-Property Gradient Text**: Every clipped gradient selector (`.gradient-text`, `.metric-number`) defines both standard `background-clip: text;` and vendor-prefixed `-webkit-background-clip: text;` with `-webkit-text-fill-color: transparent;`.
- **Fluid Metric Typography**: Metric numbers use `font-size: clamp(1.15rem, 1.8vw, 1.4rem);` paired with `word-break: break-word;` and `overflow-wrap: break-word;` to gracefully render multi-word strings (e.g., *"AWS & TIBCO"*) without container overflow.
- **Uniform Card Alignment**: Metric boxes utilize flexbox centering (`display: flex; flex-direction: column; justify-content: center; align-items: center;`) with `min-height: 86px;` to ensure consistent vertical balance across varying text lengths.

---

## ⚡ JavaScript Modules & Interactions (`script.js`)

The JavaScript layer uses pure ES6+ without external packages:

### 1. Dual Theme Engine
- Reads `localStorage.getItem('mani_theme')` on boot.
- Falls back to `window.matchMedia('(prefers-color-scheme: light)')`.
- Toggles the `data-theme` attribute on `<html>`, instantly recalibrating all CSS variable mappings.

### 2. Scroll-Linked Navigation (Intersection Observer)
- Uses `IntersectionObserver` observing all `<section id="...">` blocks.
- Automatically highlights the current active link in the sticky navigation bar based on viewport position.

### 3. Interactive Category Filter (Skills Matrix)
- Filters `.skill-tile` elements based on `data-category` attributes (`leadership`, `cloud`, `process`, or `all`).
- Applies smooth CSS transitions (`opacity`, `transform`) during filtering.

### 4. Live Timezone Clock
- Formats date and time specifically in `America/Los_Angeles` (Pacific Time) using the native `Intl.DateTimeFormat` API.
- Ticks every 1,000 milliseconds to reflect Mani's local business timezone in the SF Bay Area.

### 5. Client-Side Form Validation
- Validates name, RFC-compliant email formatting, and message body.
- Displays responsive error toasts and simulates delivery states without page reloads.

---

## 📱 Responsive Breakpoints

| Breakpoint | Target Devices | Layout Adaptations |
| :--- | :--- | :--- |
| `> 1080px` | Large Desktop / Monitors | Full multi-column grids, sidebar visual card |
| `861px – 1080px`| Small Laptops & Tablets (Landscape) | 2-column metrics and certifications grid |
| `641px – 860px` | Tablets (Portrait) | Hamburger mobile drawer, 1-column about & experience |
| `<= 640px` | Mobile Devices | Single-column cards, optimized touch targets (min 44px) |

---

## ♿ Accessibility & SEO

- **Semantic Tags**: Explicit use of `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, and `<footer>`.
- **Keyboard Navigation**: Focus rings, skip-friendly anchor tags, and accessible `aria-expanded` attributes on the mobile menu.
- **Color Contrast**: Compliant with WCAG 2.1 AA standards in both dark and light modes.
- **Metadata**: Complete Open Graph protocol tags (`og:title`, `og:description`, `og:image`, `og:url`) and structured Twitter card metadata.
