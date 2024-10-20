import {Routes, Route, createBrowserRouter, RouterProvider } from 'react-router-dom';
import './static/App.css';
import Login from "./template/auth/LoginPage";
import Index from "./template/IndexPage";

export default function App() {
  return (<>
      <header className="App-header">

      </header>
      <main>
          <div></div>
      </main>
      <footer>

      </footer>
      </>);
}

function Router(){
    return (
        <Routes>
            <Route path="*" element={<Index/>}/>
            <Route path="/app/login" element={<Login/>}/>
            <Route path="/app/login" element={<Login/>}/>
        </Routes>
    );

}

const router = createBrowserRouter([
    { path: "*", element: <Router /> },
]);
