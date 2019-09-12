from datetime import datetime, timedelta

def get_ocorrencia_monitoramento_aberta(odoo, models, localidade):
    ocorrencias = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'ocorrencia',
        'search_read',
        [
            [
                ['status_ocorrencia', '=', 1],
                ['localidade', '=', localidade],
                ['monitoramento_proativo', '=', True],
                ['create_date', '>=', (datetime.now() - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")]
            ],
        ],
        {
            'fields': [
                'id',
                'name',
                'area_resolvedora'
            ]
        }
    )

    return ocorrencias or None


def get_ocorrencia_monitoramento_fechada(odoo, models, localidade):
    ocorrencias = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'ocorrencia',
        'search_read',
        [
            [
                ['status_ocorrencia', '=', 2],
                ['localidade', '=', localidade],
                ['monitoramento_proativo', '=', True],
                ['data_ultima_normalizacao', '>=', (datetime.now() - timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")]
            ],
        ],
        {
            'fields': [
                'id',
                'name',
                'area_resolvedora'
            ]
        }
    )

    return ocorrencias or None


def abrir_ocorrencia_monitoramento(odoo, models, localidade, localidade_name, contrato):
    ocorrencia = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'ocorrencia',
        'create',
        [{
            'contrato': contrato,
            'titulo': 'Inoperância - {}'.format(localidade_name),
            'descricao': 'Detectada falha no link da localidade {}. A equipe responsável já tomou ciência, e no '
                         'momento o referido link está em análise. Em caso de dúvidas ou para maiores '
                         'informações, por gentileza contatem o suporte técnico da CINTE, através do e-mail '
                         'suporte@cinte.com.br ou pelo telefone (84)3231-2922.'.format(localidade_name),
            'tipo_ocorrencia': 34,
            'status_ocorrencia': 1,
            'localidade': localidade,
            'imputavel': 1,
            'monitoramento_proativo': True
        }]
    )

    return ocorrencia or None


def adicionar_observacao_queda_sinal(odoo, models, ocorrencia, localidade_name, area_resolvedora):
    observacao = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'abre_fecha_ocorrencia',
        'create',
        [{
            'name': '3',
            'descricao': 'O link da localidade {} ficou inoperante, estamos analisando o ocorrido.'.format(localidade_name),
            'ocorrencia': ocorrencia,
            'area_resolvedora': area_resolvedora
        }]
    )

    return observacao or None


def adicionar_observacao_retorno_sinal(odoo, models, ocorrencia, localidade_name, area_resolvedora):
    observacao = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'abre_fecha_ocorrencia',
        'create',
        [{
            'name': '3',
            'descricao': 'O link da localidade {} voltou a operar normalmente. O motivo da referida falha será exposto '
                         'no texto de fechamento desta ocorrência.'.format(localidade_name),
            'ocorrencia': ocorrencia,
            'area_resolvedora': area_resolvedora
        }]
    )

    marcar_data_ultima_normalizacao(odoo, models, ocorrencia)

    return observacao or None


def marcar_data_ultima_normalizacao(odoo, models, ocorrencia):
    operacao = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'ocorrencia',
        'write',
        [
            [ocorrencia],
            {
                'data_ultima_normalizacao': (datetime.now() + timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S")
            }
        ]
    )

    return operacao or None


def reabrir_ocorrencia(odoo, models, ocorrencia, area_resolvedora):
    reabertura = models.execute_kw(
        odoo.db, odoo.uid, odoo.password,
        'abre_fecha_ocorrencia',
        'create',
        [{
            'name': '1',
            'descricao': 'Estamos reabrindo esta ocorrência devido a falha ter reincidido.',
            'ocorrencia': ocorrencia,
            'area_resolvedora': area_resolvedora
        }]
    )

    return reabertura or None
