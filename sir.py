import matplotlib.pyplot as plt

s_cache = {}
i_cache = {}
r_cache = {}

def s(t):
	if t == 0:
		return 1

	if t in s_cache:
		value = s_cache[t]
		return value

	result = s(t-1) - (s(t-1)*i(t-1))

	s_cache[t] = result

	return result

def i(t):
	if t == 0:
		return 3.125/(10**6)

	if t in i_cache:
		value = i_cache[t]
		return value

	result = i(t-1)+(s(t-1)*i(t-1))-((1/14)*i(t-1))

	i_cache[t] = result

	return result

def r(t):
	if t == 0:
		return 0

	if t in r_cache:
		value = r_cache[t]
		return value

	result = r(t-1)+((1/14)*i(t-1))

	r_cache[t] = result

	return result

plt.figure()
s_list = []
i_list = []
r_list = []
x = [t for t in range(0,101)]
for t in range(0,101):
	s_list.append(s(t))
	i_list.append(i(t))
	r_list.append(r(t))

plt.plot(x,s_list,"r",label="s(t)")
plt.plot(x,i_list,'b',label="i(t)")
plt.plot(x,r_list,'g',label="r(t)")
plt.ylim((0, 1)) 
plt.legend()
plt.show()

print(str(s_list), file=open("output.txt", "a"))
print(str(i_list), file=open("output.txt", "a"))
print(str(r_list), file=open("output.txt", "a"))
