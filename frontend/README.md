# 🎨 GitHopper Frontend

Modern, responsive React frontend for GitHopper - providing beautiful dashboards and intuitive interfaces for repository analysis and insights.

## Overview

The frontend is built with React 18 and Vite, featuring:
- Real-time dashboard with animations
- Repository analysis visualizations
- Health score displays
- Technical debt reports
- Branch comparison tools
- Theme support (light/dark mode)
- Responsive design for all devices

## Tech Stack

- **React 18** - UI library
- **Vite 5.4** - Build tool and dev server (ultra-fast)
- **Tailwind CSS 4.2** - Utility-first CSS framework
- **React Router 7.13** - Client-side routing
- **Three.js 0.183** - 3D graphics and visualizations
- **GSAP 3.14** - Professional animation library
- **Lenis 1.3** - Smooth scrolling
- **Motion 12.38** - Animation framework
- **Firebase 12.11** - Authentication and data services

## 📋 Prerequisites

- Node.js 16 or higher
- npm or yarn package manager
- Git

## 🚀 Quick Start

### 1. Install Dependencies

```bash
npm install
# or
yarn install
```

### 2. Start Development Server

```bash
npm run dev
# or
yarn dev
```

The application will open at `http://localhost:5173`

### 3. Build for Production

```bash
npm run build
# or
yarn build
```

Creates an optimized production build in the `dist/` directory.

### 4. Preview Production Build

```bash
npm run preview
# or
yarn preview
```

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/              # Reusable React components
│   │   ├── AppLayout.jsx       # Main app layout wrapper
│   │   ├── Plasma.jsx          # 3D animated plasma background
│   │   ├── Plasma.css          # Plasma styling
│   │   ├── PlasmaBackground.jsx # Background wrapper
│   │   ├── ThemeToggle.jsx     # Light/dark mode toggle
│   │   ├── UserProfile.jsx     # User profile component
│   │   ├── ShinyText.jsx       # Animated text effect
│   │   └── [css files]         # Component-specific styling
│   │
│   ├── context/                 # React Context for state management
│   │   ├── ThemeContext.jsx    # Theme (light/dark) state
│   │   └── UserContext.jsx     # User authentication state
│   │
│   ├── pages/                   # Page components (top-level routes)
│   │   ├── HomePage.jsx        # Landing page
│   │   ├── DashboardPage.jsx   # Main dashboard
│   │   ├── AnalyseBranchesPage.jsx    # Branch analysis
│   │   ├── HealthScorePage.jsx        # Health metrics
│   │   ├── DebtReportPage.jsx         # Technical debt
│   │   ├── AuthPages.jsx              # Authentication
│   │   └── [css files]                # Page-specific styling
│   │
│   ├── services/                # API service layer
│   │   ├── api.js             # API client utilities
│   │   └── [service files]    # Domain-specific services
│   │
│   ├── main-home.jsx          # Application entry point
│   ├── styles.css             # Global styles
│   └── App.jsx                # Root component
│
├── public/                     # Static assets
│   └── assets/                # Images, icons, etc.
│
├── package.json               # Node dependencies and scripts
├── vite.config.js            # Vite configuration
├── tailwind.config.js        # Tailwind CSS configuration
├── postcss.config.js         # PostCSS (Tailwind) config
├── jsconfig.json             # JavaScript path aliases
├── components.json           # Component library config
└── README.md                 # This file
```

## 🎨 Components

### AppLayout
Main layout wrapper that provides consistent structure across all pages.

**Usage:**
```jsx
<AppLayout>
  <YourPageContent />
</AppLayout>
```

### Plasma
3D animated plasma background using Three.js. Provides a modern visual effect.

**Props:**
- `intensity` - Animation intensity (0-1)
- `speed` - Animation speed (0-2)

**Usage:**
```jsx
<Plasma intensity={0.8} speed={1} />
```

### ThemeToggle
Button to switch between light and dark themes.

**Usage:**
```jsx
<ThemeToggle />
```

### UserProfile
Displays user information and account options.

**Usage:**
```jsx
<UserProfile user={userData} />
```

## 🎯 Pages

### HomePage
Landing page with introduction and key features.

**Route:** `/`

### DashboardPage
Main dashboard showing repository overview and key metrics.

**Route:** `/dashboard`

### AnalyseBranchesPage
Compare and analyze multiple branches side-by-side.

**Route:** `/analyze-branches`

### HealthScorePage
Display code health metrics and trends.

**Route:** `/health-score`

### DebtReportPage
Technical debt analysis and recommendations.

**Route:** `/debt-report`

### AuthPages
Login, signup, and password reset pages.

**Routes:** `/login`, `/signup`, `/reset-password`

## 🌈 Theming

The application supports light and dark themes through React Context.

**Access theme in components:**
```jsx
import { useTheme } from './context/ThemeContext';

function MyComponent() {
  const { isDark, toggleTheme } = useTheme();
  
  return (
    <div className={isDark ? 'bg-gray-900' : 'bg-white'}>
      <button onClick={toggleTheme}>Toggle Theme</button>
    </div>
  );
}
```

## 🔧 Configuration

### Vite Configuration
Edit `vite.config.js` for:
- Dev server settings
- Build optimization
- Plugin configuration

### Tailwind Configuration
Edit `tailwind.config.js` for:
- Custom colors and themes
- Typography settings
- Animation/transition configs

### Environment Variables

Create a `.env` file in the frontend directory:

```env
VITE_API_BASE_URL=http://localhost:5000
VITE_FIREBASE_API_KEY=your_firebase_key
VITE_FIREBASE_AUTH_DOMAIN=your_domain
VITE_FIREBASE_PROJECT_ID=your_project_id
```

**Note:** Vite requires variables to start with `VITE_` to expose them to the client.

## 🚀 Development Workflow

### Running with Hot Module Replacement (HMR)
```bash
npm run dev
```
Changes automatically reload in the browser.

### Building a Preview
```bash
npm run build && npm run preview
```
Test the exact production build locally.

### Debugging
1. Open browser DevTools (F12)
2. Check the React tab (requires React DevTools extension)
3. Use console for logging and testing

## 📱 Responsive Design

The design uses Tailwind CSS breakpoints:
- `sm` - 640px
- `md` - 768px
- `lg` - 1024px
- `xl` - 1280px
- `2xl` - 1536px

**Example:**
```jsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
  {/* Content */}
</div>
```

## 🎬 Animations

### GSAP Animations
For complex timeline animations:

```jsx
import { useEffect } from 'react';
import gsap from 'gsap';

export function AnimatedComponent() {
  useEffect(() => {
    gsap.to('.element', { duration: 1, opacity: 1 });
  }, []);
  
  return <div className="element opacity-0">Content</div>;
}
```

### Motion Animations
For simpler animations:

```jsx
import { motion } from 'motion/react';

export function MotionComponent() {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      Content
    </motion.div>
  );
}
```

## 🔗 API Integration

### API Service Pattern

```jsx
// services/repoService.js
export async function fetchRepository(repoId) {
  const response = await fetch(
    `${import.meta.env.VITE_API_BASE_URL}/api/repos/${repoId}`
  );
  return response.json();
}

// Usage in component
import { fetchRepository } from './services/repoService';

export function RepoDetails({ repoId }) {
  const [repo, setRepo] = useState(null);
  
  useEffect(() => {
    fetchRepository(repoId).then(setRepo);
  }, [repoId]);
  
  return <div>{repo?.name}</div>;
}
```

## 🧪 Testing

### Recommended Testing Libraries
```bash
npm install --save-dev vitest @testing-library/react @testing-library/dom
```

**Example test:**
```jsx
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import MyComponent from './MyComponent';

describe('MyComponent', () => {
  it('renders correctly', () => {
    render(<MyComponent />);
    expect(screen.getByText('Expected Text')).toBeInTheDocument();
  });
});
```

## 📦 Deployment

### Building for Production
```bash
npm run build
```

### Deployment Platforms

**Vercel (Recommended for Vite):**
```bash
npm install -g vercel
vercel
```

**Netlify:**
```bash
npm run build
# Deploy the dist/ folder
```

**GitHub Pages:**
```bash
# Update vite.config.js base path
npm run build
# Push dist/ folder
```

**Docker:**
```dockerfile
FROM node:18 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:18
WORKDIR /app
RUN npm install -g serve
COPY --from=build /app/dist ./dist
EXPOSE 3000
CMD ["serve", "-s", "dist", "-l", "3000"]
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in vite.config.js or use:
npm run dev -- --port 3000
```

### Dependencies Not Installing
```bash
rm -rf node_modules package-lock.json
npm install
```

### Build Fails
```bash
# Clear cache and rebuild
rm -rf dist
npm run build
```

### Hot Module Replacement (HMR) Not Working
Check `vite.config.js` HMR configuration and browser console for errors.

## 🔗 Useful Resources

- [React Documentation](https://react.dev)
- [Vite Documentation](https://vitejs.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [React Router](https://reactrouter.com)
- [Three.js Documentation](https://threejs.org)
- [GSAP Documentation](https://gsap.com)

## 🤝 Contributing

1. Create a feature branch: `git checkout -b feature/amazing-feature`
2. Make your changes
3. Commit: `git commit -m 'Add amazing feature'`
4. Push: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

---

Built with ❤️ for GitHopper