import datetime
import sys

e = datetime.datetime.now()
print(f"<h1>processed data at {e}</h1>")

print("<pre>")
for line in sys.stdin:
  print(line)
print("</pre>")
