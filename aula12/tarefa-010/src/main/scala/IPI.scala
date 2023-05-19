import scala.io.StdIn.*
object IPI extends App{
  val ipi = readFloat()
  val cod1 = readInt()
  val val1 = readFloat()
  val qnt1 = readInt()
  val val2 = readFloat()
  val cod2 = readInt()
  val qnt2 = readInt()
  println((val1*qnt1 + val2 + qnt2)*((ipi/100) + 1))
}
