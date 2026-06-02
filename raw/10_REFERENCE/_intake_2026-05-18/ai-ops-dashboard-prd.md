# Product Requirements Document: AI Ops Dashboard

## Project Overview

Build a complete AI Opportunity Management Dashboard that helps businesses track, evaluate, and prioritise AI automation opportunities. This is a showcase project demonstrating the Ralph Wiggum technique for a YouTube tutorial.

**Target completion:** Single overnight Ralph Wiggum session
**Tech stack:** React + Tailwind CSS + Recharts (single HTML file, no build step)
**Output:** Self-contained dashboard ready to demo

---

## Success Criteria

The project is complete when ALL of the following are true:
- All 4 epics are functional and working
- The application runs without console errors
- Data persists in localStorage
- All interactive elements work (drag-drop, forms, buttons)
- Charts render correctly with real data
- Responsive on desktop (mobile is nice-to-have)

When complete, output: `<promise>DASHBOARD_COMPLETE</promise>`

---

## Architecture Overview

```
Single HTML File
├── CONFIG object (customisation points)
├── App State (React Context or useState)
│   └── opportunities[] - array of opportunity objects
├── Components
│   ├── Layout (sidebar nav + main content)
│   ├── KanbanBoard (Epic 1)
│   ├── ROICalculator (Epic 2)
│   ├── PortfolioDashboard (Epic 3)
│   └── PriorityMatrix (Epic 4)
└── localStorage persistence
```

**Data Model - Opportunity Object:**
```javascript
{
  id: "uuid",
  title: "Automate invoice processing",
  description: "Use AI to extract data from invoices",
  department: "Finance",
  status: "identified" | "evaluating" | "approved" | "implementing" | "complete",
  priority: "low" | "medium" | "high",
  // ROI fields
  hoursPerWeek: 10,
  hourlyRate: 50,
  employeesAffected: 3,
  implementationCost: 5000,
  // Calculated fields
  monthlySavings: 0,
  yearlySavings: 0,
  roiPercentage: 0,
  paybackMonths: 0,
  // Metadata
  createdAt: "2024-01-15",
  updatedAt: "2024-01-15"
}
```

---

## User Stories

### Epic 1: Kanban Board (10 stories)

**US-1.1: App Layout Shell**
As a user, I want a clean app layout with sidebar navigation so I can switch between views.

Acceptance Criteria:
- Left sidebar with navigation links: Kanban, Portfolio, Matrix
- Main content area that changes based on selected view
- App header with title "AI Ops Dashboard"
- Clean, professional design
- Kanban is the default view on load

---

**US-1.2: Kanban Board Structure**
As a user, I want to see a Kanban board with 5 columns so I can visualise the opportunity pipeline.

Acceptance Criteria:
- 5 columns: Identified → Evaluating → Approved → Implementing → Complete
- Each column has a header with title and count of cards
- Columns are horizontally scrollable on smaller screens
- Visual distinction between columns (subtle background colours)

---

**US-1.3: Opportunity Cards**
As a user, I want to see opportunity cards in the Kanban columns so I can quickly scan the pipeline.

Acceptance Criteria:
- Cards show: title, department tag, priority indicator
- Priority shown as coloured dot (red=high, yellow=medium, green=low)
- Cards have subtle shadow and rounded corners
- Cards show monthly savings if calculated (e.g., "£2,500/mo")
- Hover effect on cards

---

**US-1.4: Drag and Drop**
As a user, I want to drag cards between columns so I can update opportunity status easily.

Acceptance Criteria:
- Cards are draggable using HTML5 drag-and-drop
- Visual feedback when dragging (card opacity, drop zone highlight)
- Dropping card in new column updates its status
- State persists to localStorage after drop
- Smooth animation on drop

---

**US-1.5: Add New Opportunity**
As a user, I want to add a new opportunity so I can track new AI automation ideas.

Acceptance Criteria:
- "Add Opportunity" button visible at top of board
- Clicking opens a modal form
- Form fields: Title (required), Description, Department (dropdown), Priority (dropdown)
- New opportunities default to "Identified" column
- Form validation prevents empty title
- Modal closes on save or cancel

---

**US-1.6: Edit Opportunity**
As a user, I want to click on a card to edit its details so I can update information.

Acceptance Criteria:
- Clicking card opens edit modal
- All fields editable (title, description, department, priority)
- Save button updates the opportunity
- Cancel button discards changes
- Changes persist to localStorage

---

**US-1.7: Delete Opportunity**
As a user, I want to delete an opportunity so I can remove items that are no longer relevant.

Acceptance Criteria:
- Delete button/icon visible in edit modal
- Confirmation prompt before deletion
- Opportunity removed from state and localStorage
- UI updates immediately

---

**US-1.8: Department Filter**
As a user, I want to filter the board by department so I can focus on specific areas.

Acceptance Criteria:
- Filter dropdown above the board
- Options: All, Marketing, Sales, Finance, Operations, HR, IT
- Selecting a department shows only those cards
- "All" shows all cards
- Filter state shown visually

---

**US-1.9: Opportunity Count Summary**
As a user, I want to see a summary bar showing total opportunities and breakdown so I have a quick overview.

Acceptance Criteria:
- Summary bar above Kanban columns
- Shows: Total opportunities, count per status
- Updates dynamically when cards move
- Clean, compact design

---

**US-1.10: Empty State**
As a user, I want to see helpful messaging when the board is empty so I know how to get started.

Acceptance Criteria:
- If no opportunities exist, show empty state illustration/message
- Message: "No opportunities yet. Click 'Add Opportunity' to get started."
- Visually appealing empty state

---

### Epic 2: ROI Calculator (8 stories)

**US-2.1: ROI Tab in Edit Modal**
As a user, I want an ROI tab in the opportunity modal so I can calculate potential savings.

Acceptance Criteria:
- Edit modal has 2 tabs: "Details" and "ROI Calculator"
- Tabs switch content within the same modal
- Active tab visually highlighted

---

**US-2.2: ROI Input Fields**
As a user, I want to input ROI parameters so the system can calculate savings.

Acceptance Criteria:
- Hours per week spent on task (number input, 0-40)
- Average hourly rate (currency input, £)
- Number of employees affected (number input, 1-100)
- Estimated implementation cost (currency input, £)
- All fields have labels and placeholder text
- Inputs validate for numeric values

---

**US-2.3: ROI Calculation Engine**
As the system, I need to calculate ROI metrics when inputs change.

Calculation Logic:
```
weeklyHours = hoursPerWeek * employeesAffected
monthlyHours = weeklyHours * 4.33
automationRate = 0.75 (75% time savings assumed)
hoursReclaimed = monthlyHours * automationRate
monthlySavings = hoursReclaimed * hourlyRate
yearlySavings = monthlySavings * 12
roiPercentage = ((yearlySavings - implementationCost) / implementationCost) * 100
paybackMonths = implementationCost / monthlySavings
```

Acceptance Criteria:
- Calculations update in real-time as user types
- Results displayed below inputs
- Edge cases handled (zero values, division by zero)
- Calculated values saved to opportunity object

---

**US-2.4: ROI Results Display**
As a user, I want to see calculated ROI results clearly so I understand the potential value.

Acceptance Criteria:
- Results section shows: Monthly Savings, Yearly Savings, ROI %, Payback Period
- Large, clear typography for key numbers
- Colour coding (green for positive ROI)
- Updates live as inputs change

---

**US-2.5: ROI Visual Indicator on Cards**
As a user, I want to see ROI status on Kanban cards so I can quickly identify high-value opportunities.

Acceptance Criteria:
- Cards with ROI calculated show savings badge (e.g., "£2.5k/mo")
- Cards without ROI show "ROI not calculated" in muted text
- High ROI (>200%) gets gold badge styling

---

**US-2.6: Savings Breakdown Mini-Chart**
As a user, I want a simple visual breakdown in the ROI tab so I can see the savings composition.

Acceptance Criteria:
- Small horizontal bar showing: Hours saved vs Implementation cost
- Simple, clean visualisation
- Uses brand colours

---

**US-2.7: ROI Assumptions Note**
As a user, I want to see the assumptions used in calculations so I understand the methodology.

Acceptance Criteria:
- Collapsible "Assumptions" section in ROI tab
- Lists: 75% automation rate, 4.33 weeks/month
- Muted text styling, doesn't distract from main content

---

**US-2.8: Copy ROI Summary**
As a user, I want to copy the ROI summary to clipboard so I can share it easily.

Acceptance Criteria:
- "Copy Summary" button in ROI tab
- Copies formatted text: "Opportunity: [Title] | Monthly Savings: £X | ROI: X% | Payback: X months"
- Visual feedback on copy (button text changes briefly)

---

### Epic 3: Portfolio Dashboard (8 stories)

**US-3.1: Portfolio View Layout**
As a user, I want a Portfolio view so I can see aggregate metrics across all opportunities.

Acceptance Criteria:
- Accessible via "Portfolio" link in sidebar
- Clean dashboard layout with metric cards and charts
- Header: "Portfolio Overview"

---

**US-3.2: Summary Metric Cards**
As a user, I want to see key portfolio metrics in cards so I get an instant overview.

Acceptance Criteria:
- 4 metric cards in a grid:
  - Total Opportunities (count)
  - Total Monthly Savings (sum of all calculated)
  - Total Yearly Savings (sum)
  - Average ROI % (mean of calculated opportunities)
- Cards have icons, clear labels, large numbers
- Cards use consistent styling with Kanban

---

**US-3.3: Savings by Status Chart**
As a user, I want a chart showing savings by pipeline status so I see where value sits.

Acceptance Criteria:
- Bar chart (horizontal or vertical)
- X-axis: Status (Identified, Evaluating, Approved, Implementing, Complete)
- Y-axis: Total Monthly Savings
- Uses Recharts library
- Tooltips on hover

---

**US-3.4: Savings by Department Chart**
As a user, I want a chart showing savings by department so I see which areas have most potential.

Acceptance Criteria:
- Pie chart or donut chart
- Segments for each department with opportunities
- Legend showing department names
- Tooltips with exact values

---

**US-3.5: Pipeline Funnel Visualisation**
As a user, I want a simple funnel showing opportunity progression so I see pipeline health.

Acceptance Criteria:
- Funnel or horizontal bar showing count at each stage
- Identified → Evaluating → Approved → Implementing → Complete
- Visual shows narrowing (or not) through stages
- Simple, clear design

---

**US-3.6: Top 5 Opportunities Table**
As a user, I want to see the top 5 opportunities by savings so I know where to focus.

Acceptance Criteria:
- Table showing top 5 by monthly savings
- Columns: Rank, Title, Department, Monthly Savings, Status
- Clicking row navigates to that opportunity in Kanban
- Sorted descending by savings

---

**US-3.7: Portfolio Empty State**
As a user, I want helpful messaging when no ROI data exists so I know what to do.

Acceptance Criteria:
- If no opportunities have ROI calculated, show message
- "Add ROI data to your opportunities to see portfolio insights"
- Link/button to go to Kanban view

---

**US-3.8: Time Period Note**
As a user, I want to understand the time basis of the metrics shown.

Acceptance Criteria:
- Subtle note: "All savings shown are projected based on current data"
- Displayed below summary cards
- Muted, non-intrusive styling

---

### Epic 4: Priority Matrix (6 stories)

**US-4.1: Matrix View Layout**
As a user, I want a Priority Matrix view so I can visualise opportunities by effort vs impact.

Acceptance Criteria:
- Accessible via "Matrix" link in sidebar
- 2x2 grid layout with quadrant labels
- Header: "Priority Matrix"

---

**US-4.2: Matrix Quadrant Structure**
As a user, I want to see a 2x2 matrix so I can categorise opportunities.

Acceptance Criteria:
- X-axis: Implementation Cost (Low → High)
- Y-axis: Monthly Savings (Low → High)
- Four quadrants labelled:
  - Top-left: "Quick Wins" (high savings, low cost)
  - Top-right: "Major Projects" (high savings, high cost)
  - Bottom-left: "Fill-ins" (low savings, low cost)
  - Bottom-right: "Reconsider" (low savings, high cost)
- Quadrants have subtle background colours

---

**US-4.3: Plot Opportunities as Dots**
As a user, I want opportunities plotted as dots on the matrix so I can see the distribution.

Acceptance Criteria:
- Each opportunity with ROI data appears as a dot/circle
- Position based on implementation cost (X) and monthly savings (Y)
- Dot size could vary by employee count (nice-to-have)
- Hover shows opportunity title
- Uses Recharts ScatterChart

---

**US-4.4: Quadrant Opportunity Lists**
As a user, I want to see which opportunities fall in each quadrant so I can take action.

Acceptance Criteria:
- Below the matrix, show 4 mini-lists (one per quadrant)
- Each list shows opportunity titles in that quadrant
- Clicking an item opens the edit modal
- Lists are collapsible

---

**US-4.5: Matrix Legend**
As a user, I want a legend explaining the matrix so I understand how to interpret it.

Acceptance Criteria:
- Legend showing axis explanations
- Brief description of each quadrant's meaning
- Clean, integrated design

---

**US-4.6: Matrix Empty State**
As a user, I want helpful messaging when no opportunities can be plotted.

Acceptance Criteria:
- If no opportunities have ROI data, show message
- "Calculate ROI for opportunities to see them on the matrix"
- Link to Kanban view

---

### Epic 5: Polish & Data (5 stories)

**US-5.1: localStorage Persistence**
As a user, I want my data saved automatically so I don't lose work.

Acceptance Criteria:
- All opportunities saved to localStorage on any change
- Data loads from localStorage on app start
- Handles empty/corrupted localStorage gracefully

---

**US-5.2: Sample Data Seeding**
As a new user, I want sample data pre-loaded so I can see how the app works.

Acceptance Criteria:
- On first load (empty localStorage), seed 6-8 sample opportunities
- Opportunities spread across different statuses, departments, priorities
- 4-5 have ROI data calculated, 2-3 don't
- Varied data makes demo interesting

---

**US-5.3: Reset Data Button**
As a user, I want to reset to sample data so I can start fresh or demo again.

Acceptance Criteria:
- "Reset Demo Data" button in sidebar footer
- Confirmation prompt before reset
- Clears localStorage and reloads sample data
- App state refreshes

---

**US-5.4: Colour Scheme & Typography**
As a user, I want a professional, cohesive visual design.

Acceptance Criteria:
- Primary: Deep blue (#1e40af)
- Secondary: Green for positive/savings (#10b981)
- Accent: Purple for highlights (#7c3aed)
- Warning: Amber (#f59e0b)
- Neutral greys for backgrounds and borders
- Font: System UI stack or Inter
- Consistent spacing using Tailwind defaults

---

**US-5.5: Loading States**
As a user, I want visual feedback during any async operations.

Acceptance Criteria:
- Brief loading state on initial app load
- Skeleton or spinner while data loads
- Smooth transitions between views

---

## Technical Specifications

### Dependencies (CDN)
```html
<!-- React 18 -->
<script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- Recharts for visualisations -->
<script src="https://unpkg.com/recharts@2/umd/Recharts.min.js"></script>

<!-- UUID for generating IDs -->
<script src="https://unpkg.com/uuid@9/dist/umd/uuid.min.js"></script>
```

### File Structure (within single HTML)
```
index.html
├── <head>
│   ├── Meta tags
│   ├── CDN scripts
│   └── Tailwind config (custom colours)
├── <body>
│   └── <div id="root">
└── <script type="text/babel">
    ├── CONFIG object
    ├── SAMPLE_DATA
    ├── Helper functions (calculations, localStorage)
    ├── Context/State management
    ├── Components
    │   ├── App
    │   ├── Sidebar
    │   ├── KanbanBoard + KanbanColumn + OpportunityCard
    │   ├── OpportunityModal (with Details + ROI tabs)
    │   ├── PortfolioDashboard + MetricCard + Charts
    │   └── PriorityMatrix
    └── ReactDOM.createRoot().render()
```

---

## Completion Checklist

Before outputting the completion promise, verify:

**Epic 1 - Kanban:**
- [ ] 5-column board renders
- [ ] Cards display correctly
- [ ] Drag-and-drop works
- [ ] Add/Edit/Delete opportunities works
- [ ] Filter by department works

**Epic 2 - ROI Calculator:**
- [ ] ROI tab in modal works
- [ ] Calculations are correct
- [ ] Results display updates live
- [ ] ROI badge shows on cards

**Epic 3 - Portfolio:**
- [ ] Summary metrics calculate correctly
- [ ] Charts render with data
- [ ] Top 5 table populates

**Epic 4 - Priority Matrix:**
- [ ] 2x2 grid displays
- [ ] Opportunities plot correctly
- [ ] Quadrant lists show correct items

**Epic 5 - Polish:**
- [ ] localStorage saves/loads
- [ ] Sample data seeds on first load
- [ ] Reset button works
- [ ] No console errors