from django import template

register = template.Library()


@register.simple_tag
def texto_status(status):
    if status == 'novo':
        return 'Novo/Aguardando Avaliação do Técnico'
    elif status == 'analise':
        return 'Em Análise'
    elif status == 'draft':
        return 'Orçamento Pronto'
    elif status == 'aguardando_aprovacao':
        return 'Aguardando Aprovação'
    elif status == 'cancel':
        return 'Cancelado/Não Aprovado'
    elif status == 'confirmed':
        return 'Aprovado'
    elif status == 'aguardando_retorno':
        return 'Avisado Aguardando Retorno'
    elif status == 'teste':
        return 'Em Teste'
    elif status == 'condenado':
        return 'Sem Reparo/Condenado'
    elif status == 'under_repair':
        return 'Em Reparo'
    elif status == 'waiting_stock':
        return 'Aguardando Peças'
    elif status == 'waiting_withdrawal':
        return 'Pronto/Aguardando Retirada'
    elif status == 'done':
        return 'Reparado/Entregue'
    elif status == 'devolvido':
        return 'Devolvido/Sem Reparo'
    elif status == 'montar_devolver':
        return 'Montar P/ Devolver'
    elif status == 'descartado':
        return 'Equipamento Descartado'
    elif status == 'garantia':
        return 'Em Garantia'
    elif status == 'contato_sem_sucesso':
        return 'Tentativa de Contato S/ Sucesso'
    elif status == '2binvoiced':
        return 'Para ser Faturado'
    elif status == 'invoice_except':
        return 'Exceção de Faturamento'
    else:
        return ''
