import scala.io.StdIn.readLine
import scala.util.matching.Regex
import java.time.LocalDate
import java.time.temporal.ChronoUnit

object Age extends App {

  def calculateDays(date: List[Int]): String = date match {
    case List(years, months, days) =>
      val birthDate =
        LocalDate.now().minusDays(days).minusMonths(months).minusYears(years)
      ChronoUnit.DAYS.between(birthDate, LocalDate.now()).toString
    case _ =>
      throw new IllegalArgumentException("Invalid input.")
  }

  def formatInput(input: String): List[Int] = {
    val pattern: Regex = """\d+""".r
    val result = pattern.findAllIn(input).toList.map(_.toInt)
    if (result.length == 3) result
    else throw new IllegalArgumentException("Invalid input.")
  }

  val input = readLine()
  try {
    println(calculateDays(formatInput(input)))
  } catch {
    case ex: IllegalArgumentException => println(ex.getMessage)
  }
}
