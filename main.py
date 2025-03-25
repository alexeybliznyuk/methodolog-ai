from controller.controller import app
import uvicorn




def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8006, reload=True)

if __name__ == "__main__":
    main()

 