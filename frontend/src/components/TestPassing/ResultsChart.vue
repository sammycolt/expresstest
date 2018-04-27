<script>
import { Bar, mixins } from 'vue-chartjs'

export default {
  name: 'results-chart',
  extends: Bar,
  mixins: [mixins.reactiveProp],
  mounted () {
    // Overwriting base render method with actual data.
    this.renderChart(this.chartData)
  }
}
</script>
