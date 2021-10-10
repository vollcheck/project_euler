(require [hy.contrib.loop [loop]])


(defn collatz [n &optional [iteration 1]]
  (if (= n 1)
      iteration
      (if (= (% n 2) 0)
          (collatz (/ n 2) (inc iteration))
          (collatz (inc (* 3 n)) (inc iteration)))))


(defn find-biggest-collatz [n]
  (loop [[x 1] [max-collatz 0]]
        (if (= x n)
            x
            (if (> (collatz x) max-collatz)
                (recur (inc x) x)
                (recur (inc x) max-collatz)))))


(print (find-biggest-collatz 1_001))
