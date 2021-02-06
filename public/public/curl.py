import subprocess

def main():
    http3 = ['curl', '--http3', '-s', 'https://quic.rocks:4433/','-o','output', '-w' ,'%{time_total}']
    http2 = ['curl', '--http2', '-s', 'https://quic.rocks/','-o','output', '-w' ,'%{time_total}']
    http2Result = 0.0
    http3Result = 0.0

    for num in range(0,50):
       out_bytes1 = subprocess.check_output(http2)
       out_text1 = out_bytes1.decode('utf-8')
       http2Result = http2Result + float(out_text1) 
       out_bytes2 = subprocess.check_output(http3)
       out_text2 = out_bytes2.decode('utf-8')
       http3Result = http3Result + float(out_text2)    
    else:
       print ("http3Result:")
       print  (http3Result/50)
       print ("http2Result:")
       print  (http2Result/50)

    exit(0)

if __name__ == '__main__':
    main()
