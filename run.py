from app import create_app
import threading
import main

flask_app = create_app()

def run_flask():
    flask_app.run(debug=True, use_reloader=False)


if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True  # Il thread Flask termina con il programma
    flask_thread.start()

    main.main()
