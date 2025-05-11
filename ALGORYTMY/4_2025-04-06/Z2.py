from collections import deque
from datetime import datetime

class Notification:
    def __init__(self, content, n_type, priority="normal"):
        self.content = content
        self.type = n_type
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if n_type == "error":
            self.priority = "high"
        elif n_type == "warning":
            self.priority = "medium"
        else:
            self.priority = priority

    def __repr__(self):
        return f"[{self.priority}] {self.type.upper()}: {self.content} ({self.timestamp})"

class NotificationQueue:
    def __init__(self):
        self.queue = deque()
    
    def add_notification(self, content, n_type, priority="normal"):
        notification = Notification(content, n_type, priority)
        
        if notification.priority == "high":
            self.queue.appendleft(notification)
        elif notification.priority == "medium":
            high_priority_count = sum(1 for n in self.queue if n.priority == "high")
            self.queue.insert(high_priority_count, notification)
        else:
            self.queue.append(notification)
            self.cleanup_low_priority()

    def cleanup_low_priority(self):
        low_priority_notifications = [n for n in self.queue if n.priority == "normal"]
        while len(low_priority_notifications) > 2:
            for n in self.queue:
                if n.priority == "normal":
                    self.queue.remove(n)
                    low_priority_notifications.pop(0)
                    break

    def get_next_notification(self):
        return self.queue.popleft() if self.queue else None
    
    def pending_notifications_count(self):
        return len(self.queue)

notifications = NotificationQueue()

notifications.add_notification("Masz nowe zadanie!", "info", "normal")
notifications.add_notification("System wykrył błąd!", "error")
notifications.add_notification("Aktualizacja dostępna.", "info", "normal")
notifications.add_notification("Twoja sesja wygasła.", "warning")
notifications.add_notification("Awaria pamięci!", "error")
notifications.add_notification("Zadbaj o wzrok.", "info", "normal")
notifications.add_notification("Używkowanie na ten tydzień.", "info", "normal")
notifications.add_notification("Wróć do gry!", "info", "normal")

print("Oczekujące powiadomienia:", notifications.pending_notifications_count())

while notifications.pending_notifications_count():
    input("\nNaciśnij Enter, aby wyświetlić kolejne powiadomienie...")
    notif = notifications.get_next_notification()
    print("Wyświetl:", notif)
