```diff
--- a/src/rapo/core/main.py
+++ b/src/rapo/core/main.py
@@ -1,5 +1,18 @@
 from fastapi import FastAPI
 
+# Assuming `app` is your main FastAPI application instance
 app = FastAPI(title="RAPO API")
 
-# Any existing application routes or router includes would typically be placed here.
+# Existing application routes or router includes would typically be placed here.
+# For example:
+# from .routers import some_router
+# app.include_router(some_router.router)
+
+# Health check endpoint
+@app.get("/health", tags=["Monitoring"], summary="Service Health Check")
+async def health_check():
+    """
+    Provides a simple health check to determine if the service is running and responsive.
+    Returns a 200 OK status with a JSON payload indicating 'status: ok'.
+    """
+    return {"status": "ok"}
```