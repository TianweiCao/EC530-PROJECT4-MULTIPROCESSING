
import speech_recognition as sr
from multiprocessing import Process, Queue, Pool
import os, time
from time import sleep


# test how many process can be handled simultaneously
# 16 processes can be handled simultaneously
def convert_speech(name):
    print('start process %s (%s)...' % (name, os.getpid()))
    start = time.time()
    r = sr.Recognizer()
    with sr.AudioFile('examples_english.wav') as source:
        audio_text = r.listen(source)

        text = r.recognize_google(audio_text)


    end = time.time()
    print('process %s costs %0.2f seconds. result: %s' % (name, (end - start), text))



def run(n):
    print('main process %s.' % os.getpid())
    start = time.time()
    pool = Pool()
    for i in range(n):
        pool.apply_async(convert_speech, args=(i,))
    print('Waiting for child process to finish...')
    pool.close()
    pool.join()
    print('finisher')
    end = time.time()
    print("use {} seconds in sum".format((end - start)))


if __name__ == '__main__':
    run(14)
