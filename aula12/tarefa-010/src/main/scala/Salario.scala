import scala.io.StdIn.readFloat
object Salario extends App{
  val salMin = readFloat()
  val salUser = readFloat()
  println(s"${salUser/salMin}SM")
}
