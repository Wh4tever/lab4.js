import threading
import queue as Queue

class Token:
	def __init__(self, data, recipient):
		self.data= data
		self.recipient = recipient

def thread(i, t):
	global q
	if t.recipient == i:
		string = "TheEnd"
		q.put(string)
	else:
		print("Next")
		nextThread = threading.Thread(target=thread, name="thr", args=(i + 1, t))
		nextThread.start()

token = Token(3, 7)
q = Queue.Queue(10)

initThread = threading.Thread(target=thread, args=(1, token))
initThread.start()
print(q.get())