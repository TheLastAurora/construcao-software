object Media extends App {
  val media = (a: Float, b: Float, c: Float) => (a + b) / 2
  val med1 = media(8f, 9f, 7f)
  val med2 = media(4f, 5f, 6f)
  val soma = med1 + med2
  val med3 = (med1 + med2) / 2
  List(med1, med2, soma, med3).foreach(println(_))
}
