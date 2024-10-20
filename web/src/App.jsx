import { Routes, Route, createBrowserRouter, RouterProvider } from 'react-router-dom';
import './static/App.css';

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
        </Routes>
    );

}

const router = createBrowserRouter([
    { path: "*", element: <Router /> },
]);
