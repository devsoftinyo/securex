import os,base64_detect
fx = open("test.php","r")
fx = fx.read()
decoded = base64_detect.main(fx)
print decoded
