# Prompts & Project Changelog

A comprehensive log of all user prompts, technical decisions, problem-solving workflows, and code changes made throughout the development of the **Mani Subramanian Executive Portfolio Webpage**.

---

## 📋 Prompt History & Changes Log

### Phase 1: Webpage Generation from LinkedIn Profile

#### **Prompt:**
```text
Create a webpage for me based on the details from https://www.linkedin.com/in/manisubramanian/ 
Place the generated files under @[/Users/manisubramanian/Documents/GitHub/Day4] folder
```

#### **Challenges Encountered & Solutions:**
- **LinkedIn Anti-Scraping / Auth Wall**: LinkedIn returned HTTP status `999` on standard requests and Playwright browser binary downloads were restricted.
- **Solution**: Executed a targeted HTTP request using a macOS Chrome user-agent string to capture the full public profile page (~640 KB) and parsed the structured data (JSON-LD schema, Open Graph tags, and HTML sections).

#### **Extracted Professional Background:**
- **Executive Identity**: Senior Technical Support Leader with 15+ years of experience in enterprise support, customer escalations, and technical management.
- **Current Engagement**: Executive Leadership at **Megson Inc** (San Francisco Bay Area).
- **Tenured Leadership**: 15+ years at **TIBCO Software Inc.** as Technical Support Leader & Senior Support Manager; recipient of the **TIBCO Core Value Award**.
- **Advisory Role**: Active **Advisory Board Member for Customer Experience (CX)** at the **University of California, Irvine (UC Irvine DCE)** (Jul 2021 – Present).
- **Thought Leadership**: Published articles on LinkedIn Pulse (*"Technical Customer Support – The Tale of an Undermined Department"* and *"Corporate Lessons from Delhi Elections"*).
- **Verified Credentials**: AWS Certified Cloud Practitioner, TIBCO LEAD Certified, Kepner-Tregoe Problem Solving & Decision Making (PSDM), Salesforce Trailblazer.
- **Community Stewardship**: Concord Shiva Murugan Temple (8+ years PR Specialist), Girls in AI (Career Coach & STEM Mentor), Boy Scouts of America (Adult Leader & Treasurer), California Tamil Academy, Second Harvest Food Bank.
- **Executive Testimonials**: Authenticated quotes from technology leaders (**Ravi Desai**, **Navin Shetty**).

#### **Files Created:**
1. `index.html`: Semantic HTML5 layout with ambient lighting, stats ribbon, timeline, board advisory cards, skills matrix, community grid, recommendations, and contact form.
2. `style.css`: Vanilla CSS design system with CSS custom properties, dual theme (dark/light), glassmorphism, responsive grid layouts, and zero external framework overhead.
3. `script.js`: Vanilla ES6+ script with `localStorage` theme persistence, scroll-linked navigation (IntersectionObserver), skills filter, client-side form validation, and live SF Bay Area Pacific Time clock.
4. `README.md`: Initial project documentation and local preview instructions.

---

### Phase 2: Documentation Suite Generation

#### **Prompt:**
```text
create appropriate MD files in the same directory
```

#### **Changes & Implementation:**
Created a documentation suite to accompany the portfolio:

1. **`RESUME.md`**: Complete executive curriculum vitae in formatted Markdown, detailing executive summary, board advisory, tenured experience, certifications, publications, volunteer leadership, and colleague endorsements.
2. **`ARCHITECTURE.md`**: Technical design specifications detailing the CSS token system, color schemes, ambient lighting mechanics, JavaScript interaction modules, responsive breakpoints, and WCAG 2.1 AA accessibility guidelines.
3. **`DEPLOYMENT.md`**: Step-by-step hosting guide for GitHub Pages (zero-build deployment), custom domain DNS records (`A` and `CNAME`), Cloudflare Pages, and local development testing.
4. **`README.md`**: Updated with file trees and direct markdown links to all project documents.

---

### Phase 3: Metric Typography & Responsive Card Polish

#### **Prompt:**
```text
make these changes to the css
```
*(User highlighted lines 612–631 of `style.css` covering `.metric-box`, `.metric-number`, and `.metric-label`)*

#### **Clarification via Interactive Modal:**
- Requirement identified: Adjust font sizing and wrapping so longer labels like `"AWS & TIBCO"` fit cleanly inside the metric box without overflowing.
- Detected workspace directory rename from `Day4` to `Day3_HW`.

#### **Code Changes Applied in `Day3_HW/style.css`:**
```css
/* Enhanced Metric Box Layout */
.metric-box {
  background: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 14px 10px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 86px;
  transition: transform var(--transition-fast), border-color var(--transition-fast);
}

/* Fluid Typography and Word-Break */
.metric-number {
  display: block;
  font-family: var(--font-heading);
  font-size: clamp(1.15rem, 1.8vw, 1.4rem);
  font-weight: 800;
  line-height: 1.2;
  letter-spacing: -0.01em;
  color: var(--text-primary);
  background: var(--accent-gradient);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  word-break: break-word;
  overflow-wrap: break-word;
  max-width: 100%;
}

.metric-label {
  font-size: 0.75rem;
  line-height: 1.35;
  color: var(--text-secondary);
  font-weight: 500;
  margin-top: 4px;
}
```

---

### Phase 4: CSS Lint Warnings & Documentation Synchronization

#### **Prompt:**
```text
@[current_problems] update the MD files with the latest changes
```
*(IDE Problems block flagged: "Also define the standard property 'background-clip' for compatibility" at line 171 and line 622)*

#### **Code & Documentation Changes Applied:**
1. **Resolved CSS Compatibility Warnings (`style.css`)**:
   - Added standard `background-clip: text;` declaration directly before `-webkit-background-clip: text;` on `.gradient-text` (line 171).
   - Confirmed dual property declarations on `.metric-number` (line 630).
2. **Synchronized Documentation (`Day3_HW/`)**:
   - **`README.md`**: Updated all paths and local server commands to reference `Day3_HW`.
   - **`DEPLOYMENT.md`**: Updated build output directory and git setup instructions from `Day4` to `Day3_HW`.
   - **`ARCHITECTURE.md`**: Documented the cross-browser gradient clipping standard (`background-clip: text` + `-webkit-background-clip: text`) and fluid metric card typography rules.

---

### Phase 5: Cloud Software Group Integration & Megson Inc Account Manager Refinement

#### **Prompt:**
```text
I see that you have missed my experiences at cloud software group, and the Megson inc role is more on of account manager, go through my LinkedIn profile again and make the changes. Record all the steps in the appropriate MD files
```

#### **Analysis & Verification Steps:**
1. Cross-referenced profile records and advisory listings confirming Mani's tenure as **Senior Technical Support Manager** at **Cloud Software Group (CSG)** based in Santa Clara, California, managing enterprise technical operations post-merger of TIBCO Software and Citrix.
2. Clarified and restructured the **Megson Inc** role to **Account Manager**, focusing on enterprise client relationship governance, client retention, executive QBRs, and customer advocacy.
3. Preserved the tenured 15+ years foundational journey at **TIBCO Software Inc.** as Senior Technical Support Manager and recipient of the **TIBCO Core Value Award**.

#### **Code & Documentation Changes Applied:**
1. **`index.html`**:
   - Updated page title, description, and Open Graph social metadata.
   - Updated navbar brand subtitle: `Account Manager • Tech Support Leader`.
   - Updated hero headline and description highlighting dual expertise in strategic account management and technical support across Cloud Software Group, TIBCO, and Megson Inc.
   - Added **Cloud Software Group (CSG)** to the career timeline as **Senior Technical Support Manager** (Santa Clara, CA).
   - Refined **Megson Inc** entry to **Account Manager**, detailing account expansion, retention, and executive QBR governance.
   - Updated footer credentials and branding.
2. **`RESUME.md`**:
   - Updated executive title to **Account Manager & Senior Technical Support Leader**.
   - Added full dedicated experience block for **Cloud Software Group (CSG)** with bullet points on Tier-1 escalations, post-merger support workflows, and 24/7 global operations.
   - Updated **Megson Inc** experience block to detail Account Manager responsibilities (client retention, churn mitigation, SLA governance).
3. **`README.md`**:
   - Synchronized executive identity and background bullet points.

---

## 🗂️ Current Repository File Map (`Day3_HW`)

| File | Purpose |
| :--- | :--- |
| [`index.html`](index.html) | Semantic HTML5 structure with executive layout and SEO tags |
| [`style.css`](style.css) | Design tokens, responsive grid, dual themes, and glassmorphism |
| [`script.js`](script.js) | Theme switcher, navigation observer, category filter, live clock |
| [`README.md`](README.md) | Project overview, feature summary, and quick start guide |
| [`RESUME.md`](RESUME.md) | Executive CV and verified professional profile in Markdown |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Technical architecture, design token dictionary, and layout specs |
| [`DEPLOYMENT.md`](DEPLOYMENT.md) | Deployment instructions for GitHub Pages, Cloudflare, and custom DNS |
| [`PROMPTS_AND_CHANGELOG.md`](PROMPTS_AND_CHANGELOG.md) | Chronological prompt history, technical resolutions, and diff logs |
