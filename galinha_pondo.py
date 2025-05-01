import time
import sys

def botar_ovo():
    print("🐔 A galinha vai botar um ovo...")
    for i in range(1, 11):
        sys.stdout.write('\r' + '🥚' * i)
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n🎉 A galinha botou o ovo! Viva o sertão!")

def main():
    botar_ovo()

if __name__ == "__main__":
    main()
