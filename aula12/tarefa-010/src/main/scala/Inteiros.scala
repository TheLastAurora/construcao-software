import scala.io.StdIn.readInt
object Inteiros extends App {
  val num = readInt()
  println(s"antecessor: ${num-1}\nsucessor: ${num+1}")
}
