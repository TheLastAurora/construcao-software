import scala.io.StdIn

object IPI extends App {
  val ipi = StdIn.readFloat()
  val cod1 = StdIn.readInt()
  val val1 = StdIn.readFloat()
  val qnt1 = StdIn.readInt()
  val val2 = StdIn.readFloat()
  val cod2 = StdIn.readInt()
  val qnt2 = StdIn.readInt()
  println((val1 * qnt1 + val2 * qnt2) * ((ipi / 100) + 1))
}
