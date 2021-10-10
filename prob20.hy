(defn factorial-digit-sum [n]
  (sum (map int (str (reduce * (range 1 (+ n 1)))))))
