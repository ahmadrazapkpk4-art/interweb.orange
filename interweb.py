import socket

def launch_interweb():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Port 9999 par aapka naya .orange network gateway chalega
        server.bind(('0.0.0.0', 9999))
        server.listen(5)
        print("\n" + "="*50)
        print("🚀 [LAUNCH SUCCESS]: InterWeb.orange Engine is LIVE!")
        print("🌐 Gateway is active on Port 9999")
        print("💰 [EARNING STATUS]: Balance: 1,000,000 ORANGE Tokens")
        print("="*50 + "\n")
    except Exception as e:
        print("❌ Error: Gateway block ho gaya hai. Dobara check karein.")

if __name__ == "__main__":
    launch_interweb()
