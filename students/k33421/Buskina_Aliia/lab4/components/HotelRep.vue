<template>
  <div class="quarterly-report">
    <h2>Generate Quarterly Report</h2>
    <form @submit.prevent="generateReport">
      <label for="startDate">Start Date:</label>
      <input type="date" v-model="startDate" required />

      <label for="endDate">End Date:</label>
      <input type="date" v-model="endDate" required />

      <button type="submit">Generate Report</button>
    </form>

    <div v-if="reportData !== null">
      <h3>Quarterly Report</h3>

      <!-- Displaying room_client_reports -->
      <div v-if="reportData.reports.length > 0">
        <h4>Room Client Reports</h4>
        <ul>
          <li v-for="(report, idx) in reportData.reports" :key="idx">
            Room {{ report.room_id }}: {{ report.guests_count }} clients, Income: {{ report.room_income }}
          </li>
        </ul>
      </div>

      <!-- Displaying floor_reports -->
      <div v-if="reportData.floor_counts.length > 0">
        <h4>Floor Reports</h4>
        <ul>
          <li v-for="(report, idx) in reportData.floor_counts" :key="idx">
            Floor {{ report.floor }}: {{ report.room_count }} rooms
          </li>
        </ul>
      </div>

      <!-- Displaying total_income_for_room -->
      <div v-if="reportData.total_income !== null">
        <h4>Total Income for Hotel</h4>
        <p>{{ reportData.total_income }}</p>
      </div>
    </div>
    <div v-else>
      <p>No report generated yet.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      startDate: '',
      endDate: '',
      reportData: null,
    };
  },
  methods: {
    async generateReport() {
      try {
        const response = await this.$http.get(`http://127.0.0.1:8000/api/quarterly_report/${this.startDate}/${this.endDate}/`);
        this.reportData = response.data;
      } catch (error) {
        console.error('Error generating report:', error.message || error);
      }
    },
  },
};
</script>
