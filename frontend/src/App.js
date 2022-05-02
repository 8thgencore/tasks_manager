import React from "react";
import ReactDOM from "react-dom";
import { Box, CssBaseline } from "@mui/material";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Categories from "./pages/Categories";
import CategoryDetails from "./pages/Categories/CategoryDetails";
import { SnackbarProvider } from "notistack";

export default function App() {
  return (
    <div>
      <CssBaseline />
      <SnackbarProvider>
        <Router>
          <Box
            sx={{
              bgcolor: (theme) => theme.palette.background.default,
              minHeight: "100vg",
            }}
          >
            <Routes>
              <Route path="/categories" element={<Categories />} />
              <Route path="/categories/create" element={<CategoryDetails />} />
              <Route path={`/categories/edit/:id`} element={<CategoryDetails />} />
            </Routes>
          </Box>
        </Router>
      </SnackbarProvider>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
