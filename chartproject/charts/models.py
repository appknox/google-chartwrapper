from django.db import models
    
class Chart(models.Model):
    name = models.CharField(max_length=255)
    data = models.TextField()
    chart_instructions = models.TextField()
            
    def __str__(self):
        return ' | '.join(self.chart_instructions.splitlines()[:-1])
            
    class Admin: pass
                        

