# Healthcare System Frontend

A modern, responsive frontend for the Online Healthcare System built with React.js, TypeScript, and Tailwind CSS.

## Project Structure

```
frontend/
├── src/
│   ├── components/         # Reusable UI components
│   │   ├── common/        # Common components like buttons, inputs, etc.
│   │   ├── layout/        # Layout components like navbar, footer, etc.
│   │   └── sections/      # Page-specific sections
│   ├── pages/             # Page components
│   │   ├── Home/
│   │   ├── Dashboard/
│   │   ├── Appointments/
│   │   ├── MedicalReports/
│   │   ├── Prescriptions/
│   │   ├── Payments/
│   │   └── Feedback/
│   ├── hooks/             # Custom React hooks
│   ├── context/           # React context providers
│   ├── services/          # API services
│   ├── utils/             # Utility functions
│   ├── types/             # TypeScript type definitions
│   ├── assets/            # Static assets (images, icons, etc.)
│   └── styles/            # Global styles and Tailwind config
└── public/                # Public assets
```

## Features

- 🎨 Modern and Professional UI
- 📱 Fully Responsive Design
- 🌓 Dark & Light Mode
- 🔄 Smooth Animations
- 🔒 Secure Authentication
- 📅 Interactive Calendar
- 🔍 Advanced Search & Filter
- 📤 File Upload System
- 💬 Feedback System

## Tech Stack

- React.js with TypeScript
- Tailwind CSS for styling
- React Router for navigation
- React Query for API data management
- Headless UI for accessible components
- Hero Icons for beautiful icons
- React Hook Form for form handling
- Zod for form validation
- Axios for API requests
- Day.js for date handling
- React Hot Toast for notifications

## Setup Instructions

1. Install Node.js (v16 or later)
2. Clone the repository
3. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
4. Create a `.env` file with required environment variables
5. Start the development server:
   ```bash
   npm start
   ```

## Development Guidelines

1. **Component Structure**
   - Use functional components with TypeScript
   - Implement proper type definitions
   - Follow React best practices

2. **Styling**
   - Use Tailwind CSS utility classes
   - Follow mobile-first approach
   - Maintain consistent spacing and colors

3. **State Management**
   - Use React Context for global state
   - Implement proper loading states
   - Handle errors gracefully

4. **Code Quality**
   - Write clean, documented code
   - Follow ESLint rules
   - Add proper comments

5. **Performance**
   - Implement code splitting
   - Use lazy loading for images
   - Optimize bundle size

## Available Scripts

- `npm start` - Start development server
- `npm test` - Run tests
- `npm run build` - Build for production
- `npm run lint` - Run ESLint
- `npm run format` - Format code with Prettier

## Contributing

1. Follow the coding guidelines
2. Write meaningful commit messages
3. Test your changes thoroughly
4. Create detailed pull requests 