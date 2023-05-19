import scala.io.StdIn

object Salario extends App {
  val salMin = StdIn.readFloat()
  val salUser = StdIn.readFloat()
  println(s"${salUser / salMin} SM")
}
