import scala.annotation.tailrec
import scala.sys._
import scala.io.StdIn.readLine
object Solution {
  def main(args: Array[String]): Unit = {

    val nums = readLine.split(" ").map(_.toInt).toList

    println(canSurface(nums, nums.head))

  }

  @tailrec
  def canSurface(nums: List[Int], fuel: Int): Int = {

    //We made it to the end
    if (nums.tail == Nil) {
      return 1
    }
    val maxFuel = fuel.max(nums.head)

    //We can reach the end on the current tank, no need to calculate the rest
    if (maxFuel >= nums.length - 1) {
      return 1
    }

    //we can't go any longer
    if (maxFuel < 1) {
      return 0
    }

    canSurface(nums.tail, maxFuel - 1)
  }
}

