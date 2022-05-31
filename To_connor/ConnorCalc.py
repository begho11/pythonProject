# Test calculator application.py
from CalculateBMI import hlthCalculator as c

class TestCalculatorAppInstance():
    bmi_df = c.calculate_BMI(c.return_data())
    health_risk_df = c.assign_health_risk(bmi_df)

    def test_weight_for_null_values(self):
        health_risk_df = self.health_risk_df
        counter = health_risk_df['HeightCm'].isna().sum()
        assert counter == 0

    def test_height_for_null_values(self):
        health_risk_df = self.health_risk_df
        counter = health_risk_df['WeightKg'].isna().sum()
        assert counter == 0

    def test_BMI_for_null_values(self):
        health_risk_df = self.health_risk_df
        counter = health_risk_df['BMI'].isna().sum()
        assert counter == 0

    def test_Count_of_overwight(self):
        health_risk_df = self.health_risk_df
        counter = len(health_risk_df[(health_risk_df["BMI"] >= 25) &(health_risk_df["BMI"] <= 29.9)])
        assert counter == 0

    def test_source_and_dest_volume(self):
        s_count = len(self.bmi_df)
        target_count = len(self.health_risk_df)
        assert s_count == target_count
