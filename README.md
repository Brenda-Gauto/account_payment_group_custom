# account_payment_group_custom
Recibos de pago clientes/proveedores modificado

Verificar para la instalación lo siguiente:

  - Los campos computados matched_amount y unmatched_amount del modelo account_payment_group.py deben tener sin comentar el *compute = '_compute_matched_amounts'*
  - La funcion *_compute_matched_amounts* debe quedar de la siguiente manera:
<html>
  def _compute_matched_amounts(self):
        for rec in self:
            if rec.state != 'posted':
                rec.matched_amount = 0
                rec.unmatched_amount = 0
            if not rec.partner_id:
                rec.matched_amount = 0
                rec.unmatched_amount = 0
            # damos vuelta signo porque el payments_amount tmb lo da vuelta,
            # en realidad porque siempre es positivo y se define en funcion
            # a si es pago entrante o saliente
            sign = rec.partner_type == 'supplier' and -1.0 or 1.0
            if rec.state == 'posted':
                rec.matched_amount = sign * sum(
                    rec.matched_move_line_ids.with_context(
                        payment_group_id=rec.id).mapped(
                            'payment_group_matched_amount'))
                rec.unmatched_amount = rec.payments_amount - rec.matched_amount
            else:
                rec.matched_amount = 0
                rec.unmatched_amount = 0

</html>
