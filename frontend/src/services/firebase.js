import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import { getAnalytics } from "firebase/analytics";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBMxfOSo8jKEOOrD9GmTyAtjl5JPewEvMA",
    authDomain: "githopper.firebaseapp.com",
    projectId: "githopper",
    storageBucket: "githopper.firebasestorage.app",
    messagingSenderId: "364587244760",
    appId: "1:364587244760:web:bfb125235ebffdcbd88bad",
    measurementId: "G-64TYKKN7RH"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const analytics = getAnalytics(app);
const googleProvider = new GoogleAuthProvider();

export { app, auth, analytics, googleProvider, signInWithPopup };
