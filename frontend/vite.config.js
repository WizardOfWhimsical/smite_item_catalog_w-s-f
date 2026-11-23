import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";
import { execFileSync } from "child_process";

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    {
      name: "python-bridge",
      configureServer(server) {
        server.middlewares.use("/v1/api/py_backend", (req, res) => {
          try {
            const output = execFileSync(
              "python3",
              ["../BackEnd/record_items_code.py"],
              { encoding: "utf8" },
            );
            res.setHeader("Content-Type", "application/json");
            res.end(output);
          } catch (error) {
            res.statusCode = 500;
            res.end(JSON.stringify({ error: error.message }));
          }
        });
      },
    },
  ],
});
