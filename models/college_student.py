from odoo import models , fields

class CollegeSudent(models.Model):
    _name = "college.student"
    _description = "College Student"
    
    admission_no = fields.Char(string="Admission Name" , required = True)