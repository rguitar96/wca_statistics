#   pip install pymysql
#   pip install matplotlib
#   pip install numpy
import pymysql
import matplotlib
import matplotlib.pyplot as plt
import numpy
import datetime
import time


def graficas_competiciones():
    #   NUMERO DE CAMPEONATOS EN EL MUNDO / ESPAÑA POR AÑO
    #   formato:
    #   SELECT COUNT(*) FROM wca_export.competitions WHERE year=2005
    print("Comenzando el análisis de las estadísticas de competiciones. ", time.time() - start_time, "segundos")
    year = 1982
    world_years = []
    world_comps = []
    spain_comps = []
    world_ncomps = 0
    spain_ncomps = 0
    while (actual_year>=year):
        sql = 'SELECT COUNT(*) FROM wca_export.competitions WHERE year='
        sql += str(year)
        if (actual_year==year):
            sql += ' AND month<'
            sql += str(actual_month)
        cursor.execute(sql)
        data = cursor.fetchone()
        if (data[0]>0):
            world_years.append(str(year))
            world_comps.append(data[0])
            world_ncomps += data[0]

        sql += ' AND countryId=\'Spain\''
        cursor.execute(sql)
        data = cursor.fetchone()
        print("Terminado el análisis de ",year, ". ", time.time() - start_time, "segundos")
        if (data[0]>0 or year==2003 or year==1982):
            spain_comps.append(data[0])
            spain_ncomps += data[0]
        year += 1
    print("Terminado el análisis de las estadísticas de competiciones. ", time.time() - start_time, "segundos")

    #   GRÁFICAS COMPETICIONES
    y_pos = numpy.arange(len(world_years))

    fig_size = (12,9)
    plt.rcParams["figure.figsize"] = fig_size
    plt.text(7.03, max(spain_comps), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, spain_comps, align='center', alpha=0.5)
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de campeonatos')
    plt.title('Campeonatos anuales en España (hasta el 01/07/2018)')
    plt.savefig('campeonatos_anuales_s.png')
    plt.close()

    plt.text(7.03, max(world_comps), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, world_comps, align='center', alpha=0.5)
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de campeonatos')
    plt.title('Campeonatos anuales en el mundo (hasta el 01/07/2018)')
    plt.savefig('campeonatos_anuales_w.png')
    plt.close()

    plt.text(7.03, max(world_comps)-(max(world_comps)*0.07), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, world_comps, align='center', alpha=0.5, label = 'Mundial')
    plt.bar(y_pos, spain_comps, align='center', alpha=0.5, label = 'España')
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de campeonatos')
    plt.title('Campeonatos anuales en el mundo y en España (hasta el 01/07/2018)')
    plt.legend(loc='upper left')
    plt.savefig('campeonatos_anuales_ws.png')
    plt.close()


    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    plt.title('Estadísticas sobre el número de campeonatos en España y en el mundo')
    percentages = []
    for i in range(0, len(world_years)):
        percentages.append(round(spain_comps[i]/(world_comps[i]/100),2))
    clust_data = numpy.array( [numpy.array(world_comps),numpy.array(spain_comps),numpy.array(percentages)] )
    rowlabel=("En el mundo", "En España", "En España sobre el total (%)")
    ax.table(cellText=clust_data, colLabels=numpy.array(world_years),rowLabels=rowlabel, 
            bbox=[0.1, 0.5, 1.0, 0.5],rowColours=['gray']*3, colColours=['gray']*17)
    plt.savefig('estadisticas_campeonatos.png')
    plt.close()

    print("Se han generado los archivos correspondientes. ", time.time() - start_time, "segundos")

def graficas_resultados():
    #   NUMERO DE RESOLUCIONES EN EL MUNDO / ESPAÑA POR AÑO
    #   formato:
    #   SELECT * FROM wca_export.results
    #   INNER JOIN wca_export.competitions
    #   ON wca_export.results.competitionId=wca_export.competitions.id
    #   WHERE year = 2005;
    print("Comenzando el análisis de las estadísticas de resultados. ", time.time() - start_time, "segundos")
    year = 1982
    world_years = []
    world_results = []
    spain_results = []
    world_nresults = 0
    spain_nresults = 0
    while (actual_year>=year):
        sql = 'SELECT COUNT(*) FROM wca_export.results INNER JOIN wca_export.competitions ON wca_export.results.competitionId=wca_export.competitions.id WHERE year='
        sql += str(year)
        if (actual_year==year):
            sql += ' AND month<'
            sql += str(actual_month)
        cursor.execute(sql)
        data = cursor.fetchone()
        if (data[0]>0):
            world_years.append(str(year))
            world_results.append(data[0])
            world_nresults += data[0]

        sql += ' AND countryId=\'Spain\''
        cursor.execute(sql)
        data = cursor.fetchone()
        print("Terminado el análisis de ",year, time.time() - start_time, "segundos")
        if (data[0]>0 or year==2003 or year==1982):
            spain_results.append(data[0])
            spain_nresults += data[0]
        year += 1
    print("Terminado el análisis de las estadísticas de resultados. ", time.time() - start_time, "segundos")

    #   GRÁFICAS RESULTADOS
    y_pos = numpy.arange(len(world_years))

    fig_size = (12,9)
    plt.rcParams["figure.figsize"] = fig_size

    plt.text(7.03, max(spain_results), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, spain_results, align='center', alpha=0.5)
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de resoluciones')
    plt.title('Resoluciones anuales en España (hasta el 01/07/2018)')
    plt.savefig('resoluciones_anuales_s.png')
    plt.close()

    plt.text(7.03, max(world_results), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, world_results, align='center', alpha=0.5)
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de resoluciones')
    plt.title('Resoluciones anuales en el mundo (hasta el 01/07/2018)')
    plt.savefig('resoluciones_anuales_w.png')
    plt.close()

    plt.text(7.03, max(world_results)-(max(world_results)*0.07), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, world_results, align='center', alpha=0.5, label = 'Mundial')
    plt.bar(y_pos, spain_results, align='center', alpha=0.5, label = 'España')
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de resoluciones')
    plt.title('Resoluciones anuales en el mundo y en España (hasta el 01/07/2018)')
    plt.legend(loc='upper left')
    plt.savefig('resoluciones_anuales_ws.png')
    plt.close()

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    plt.title('Estadísticas sobre el número de resoluciones en España y en el mundo')
    percentages = []
    for i in range(0, len(world_years)):
        percentages.append(round(spain_results[i]/(world_results[i]/100),2))
    clust_data = numpy.array( [numpy.array(world_results),numpy.array(spain_results),numpy.array(percentages)] )
    rowlabel=("En el mundo", "En España", "En España sobre el total (%)")
    ax.table(cellText=clust_data, colLabels=numpy.array(world_years),rowLabels=rowlabel, 
            bbox=[0.1, 0.5, 1.0, 0.5],rowColours=['gray']*3, colColours=['gray']*17)
    plt.savefig('estadisticas_resoluciones.png')
    plt.close()
    print("Se han generado los archivos correspondientes. ", time.time() - start_time, "segundos")


def graficas_rondas():
    #   NUMERO DE RONDAS EN EL MUNDO / ESPAÑA POR AÑO
    #   formato:
    #   SELECT COUNT(*) FROM (
    #     SELECT DISTINCT competitionId, eventId, roundTypeId, personId FROM wca_export.results
    #   	INNER JOIN wca_export.competitions
    #   	ON wca_export.results.competitionId=wca_export.competitions.id
    #   	WHERE year = 2005
    #   ) AS x
    print("Comenzando el análisis de las estadísticas de rondas. ", time.time() - start_time, "segundos")
    year = 1982
    world_years = []
    world_rounds = []
    spain_rounds = []
    world_nrounds = 0
    spain_nrounds = 0
    while (actual_year>=year):
        sql = 'SELECT COUNT(*) FROM (SELECT DISTINCT competitionId, eventId, roundTypeId, personId FROM wca_export.results INNER JOIN wca_export.competitions ON wca_export.results.competitionId=wca_export.competitions.id WHERE year ='
        sql += str(year)
        if (actual_year==year):
            sql += ' AND month<'
            sql += str(actual_month)
        sql += ') AS x'
        cursor.execute(sql)
        data = cursor.fetchone()
        print("Terminado el análisis de ",year, time.time() - start_time, "segundos")
        if (data[0]>0):
            world_years.append(str(year))
            world_rounds.append(data[0])
            world_nrounds += data[0]

        sql = sql.replace(') AS x','')
        sql += ' AND countryId=\'Spain\''
        sql += ') AS x'
        cursor.execute(sql)
        data = cursor.fetchone()
        if (data[0]>0 or year==2003 or year==1982):
            spain_rounds.append(data[0])
            spain_nrounds += data[0]
        year += 1
    print("Terminado el análisis de las estadísticas de rondas. ", time.time() - start_time, "segundos")

    #   GRÁFICAS RONDAS
    y_pos = numpy.arange(len(world_years))

    fig_size = (12,9)
    plt.rcParams["figure.figsize"] = fig_size

    plt.text(7.03, max(spain_rounds), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, spain_rounds, align='center', alpha=0.5)
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de rondas')
    plt.title('Rondas por competidor anuales en España (hasta el 01/07/2018)')
    plt.savefig('rondas_anuales_s.png')
    plt.close()

    plt.text(7.03, max(world_rounds), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, world_rounds, align='center', alpha=0.5)
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de rondas')
    plt.title('Rondas por competidor anuales en el mundo (hasta el 01/07/2018)')
    plt.savefig('rondas_anuales_w.png')
    plt.close()

    plt.text(7.03, max(world_rounds)-(max(world_rounds)*0.07), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, world_rounds, align='center', alpha=0.5, label = 'Mundial')
    plt.bar(y_pos, spain_rounds, align='center', alpha=0.5, label = 'España')
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de rondas')
    plt.title('Rondas por competidor anuales en el mundo y en España (hasta el 01/07/2018)')
    plt.legend(loc='upper left')
    plt.savefig('rondas_anuales_ws.png')
    plt.close()

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    plt.title('Estadísticas sobre el número de rondas por competidor en España y en el mundo')
    percentages = []
    for i in range(0, len(world_years)):
        percentages.append(round(spain_rounds[i]/(world_rounds[i]/100),2))
    clust_data = numpy.array( [numpy.array(world_rounds),numpy.array(spain_rounds),numpy.array(percentages)] )
    rowlabel=("En el mundo", "En España", "En España sobre el total (%)")
    ax.table(cellText=clust_data, colLabels=numpy.array(world_years),rowLabels=rowlabel, 
            bbox=[0.1, 0.5, 1.0, 0.5],rowColours=['gray']*3, colColours=['gray']*17)
    plt.savefig('estadisticas_rondas.png')
    plt.close()
    print("Se han generado los archivos correspondientes. ", time.time() - start_time, "segundos")


def graficas_nuevaspersonas():
    #   NUMERO DE COMPETIDORES NUEVOS EN EL MUNDO / ESPAÑA POR AÑO
    #   formato:
    #   SELECT COUNT(*) FROM wca_export.persons WHERE id LIKE '%1982%'
    print("Comenzando el análisis de las estadísticas de nuevos competidores. ", time.time() - start_time, "segundos")
    year = 1982
    world_years = []
    world_newcompetitors = []
    spain_newcompetitors = []
    world_nnewcompetitors = 0
    spain_nnewcompetitors = 0
    while (actual_year>=year):
        sql = 'SELECT COUNT(*) FROM wca_export.persons WHERE id LIKE \'%'
        sql += str(year)
        sql += str('%\'')
        cursor.execute(sql)
        data = cursor.fetchone()
        if (data[0]>0):
            world_years.append(str(year))
            world_newcompetitors.append(data[0])
            world_nnewcompetitors += data[0]

        sql += ' AND countryId=\'Spain\''
        cursor.execute(sql)
        data = cursor.fetchone()
        print("Terminado el análisis de ",year, time.time() - start_time, "segundos")
        if (data[0]>0 or year==2003 or year==1982):
            spain_newcompetitors.append(data[0])
            spain_nnewcompetitors += data[0]
        year += 1
    print("Terminado el análisis de las estadísticas de nuevos competidores. ", time.time() - start_time, "segundos")

    #   GRÁFICAS NUEVAS PERSONAS
    y_pos = numpy.arange(len(world_years))

    fig_size = (12,9)
    plt.rcParams["figure.figsize"] = fig_size

    plt.text(7.03, max(spain_newcompetitors), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, spain_newcompetitors, align='center', alpha=0.5)
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de competidores')
    plt.title('Nuevos competidores anuales en España (hasta el 01/07/2018)')
    plt.savefig('nuevoscompetidores_anuales_s.png')
    plt.close()

    plt.text(7.03, max(world_newcompetitors), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, world_newcompetitors, align='center', alpha=0.5)
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de competidores')
    plt.title('Nuevos competidores anuales en el mundo (hasta el 01/07/2018)')
    plt.savefig('nuevoscompetidores_anuales_w.png')
    plt.close()

    plt.text(7.03, max(world_newcompetitors)-(max(world_newcompetitors)*0.07), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, world_newcompetitors, align='center', alpha=0.5, label = 'Mundial')
    plt.bar(y_pos, spain_newcompetitors, align='center', alpha=0.5, label = 'España')
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de competidores')
    plt.title('Nuevos competidores anuales en el mundo y en España (hasta el 01/07/2018)')
    plt.legend(loc='upper left')
    plt.savefig('nuevoscompetidores_anuales_ws.png')
    plt.close()

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    plt.title('Estadísticas sobre el número de nuevos competidores en España y en el mundo')
    percentages = []
    for i in range(0, len(world_years)):
        percentages.append(round(spain_newcompetitors[i]/(world_newcompetitors[i]/100),2))
    clust_data = numpy.array( [numpy.array(world_newcompetitors),numpy.array(spain_newcompetitors),numpy.array(percentages)] )
    rowlabel=("En el mundo", "En España", "En España sobre el total (%)")
    ax.table(cellText=clust_data, colLabels=numpy.array(world_years),rowLabels=rowlabel, 
            bbox=[0.1, 0.5, 1.0, 0.5],rowColours=['gray']*3, colColours=['gray']*17)
    plt.savefig('estadisticas_nuevoscompetidores.png')
    plt.close()
    print("Se han generado los archivos correspondientes. ", time.time() - start_time, "segundos")


def graficas_personasunicas():
    #   NUMERO DE COMPETIDORES ÚNICOS EN EL MUNDO / ESPAÑA POR AÑO
    #   formato:
    #   SELECT COUNT(*) FROM (
    #   SELECT DISTINCT year, personId FROM wca_export.results
    #   INNER JOIN wca_export.competitions
    #   ON wca_export.results.competitionId=wca_export.competitions.id
    #   WHERE year = 2005
    #   ) AS x
    print("Comenzando el análisis de las estadísticas de competidores únicos. ", time.time() - start_time, "segundos")
    year = 1982
    world_years = []
    world_uniquecompetitors = []
    spain_uniquecompetitors = []
    world_nuniquecompetitors = 0
    spain_nuniquecompetitors = 0
    while (actual_year>=year):
        sql = 'SELECT COUNT(*) FROM (SELECT DISTINCT year, personId FROM wca_export.results INNER JOIN wca_export.competitions ON wca_export.results.competitionId=wca_export.competitions.id WHERE year ='
        sql += str(year)
        if (actual_year==year):
            sql += ' AND month<'
            sql += str(actual_month)
        sql += ') AS x'
        cursor.execute(sql)
        data = cursor.fetchone()
        print("Terminado el análisis de ",year, time.time() - start_time, "segundos")
        if (data[0]>0):
            world_years.append(str(year))
            world_uniquecompetitors.append(data[0])
            world_nuniquecompetitors += data[0]

        sql = sql.replace(') AS x','')
        sql += ' AND countryId=\'Spain\''
        sql += ') AS x'
        cursor.execute(sql)
        data = cursor.fetchone()
        if (data[0]>0 or year==2003 or year==1982):
            spain_uniquecompetitors.append(data[0])
            spain_nuniquecompetitors += data[0]
        year += 1
    print("Terminado el análisis de las estadísticas de competidores únicos. ", time.time() - start_time, "segundos")

    #   GRÁFICAS PERSONAS ÚNICAS
    y_pos = numpy.arange(len(world_years))

    fig_size = (12,9)
    plt.rcParams["figure.figsize"] = fig_size

    plt.text(7.03, max(spain_uniquecompetitors), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, spain_uniquecompetitors, align='center', alpha=0.5)
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de competidores')
    plt.title('Competidores únicos anuales en España (hasta el 01/07/2018)')
    plt.savefig('competidoresunicos_anuales_s.png')
    plt.close()

    plt.text(7.03, max(world_uniquecompetitors), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, world_uniquecompetitors, align='center', alpha=0.5)
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de competidores')
    plt.title('Competidores únicos anuales en el mundo (hasta el 01/07/2018)')
    plt.savefig('competidoresunicos_anuales_w.png')
    plt.close()

    plt.text(7.03, max(world_uniquecompetitors)-(max(world_uniquecompetitors)*0.07), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, world_uniquecompetitors, align='center', alpha=0.5, label = 'Mundial')
    plt.bar(y_pos, spain_uniquecompetitors, align='center', alpha=0.5, label = 'España')
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de competidores')
    plt.title('Competidores únicos anuales en el mundo y en España (hasta el 01/07/2018)')
    plt.legend(loc='upper left')
    plt.savefig('competidoresunicos_anuales_ws.png')
    plt.close()

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    plt.title('Estadísticas sobre el número de competidores únicos en España y en el mundo')
    percentages = []
    for i in range(0, len(world_years)):
        percentages.append(round(spain_uniquecompetitors[i]/(world_uniquecompetitors[i]/100),2))
    clust_data = numpy.array( [numpy.array(world_uniquecompetitors),numpy.array(spain_uniquecompetitors),numpy.array(percentages)] )
    rowlabel=("En el mundo", "En España", "En España sobre el total (%)")
    ax.table(cellText=clust_data, colLabels=numpy.array(world_years),rowLabels=rowlabel, 
            bbox=[0.1, 0.5, 1.0, 0.5],rowColours=['gray']*3, colColours=['gray']*17)
    plt.savefig('estadisticas_competidoresunicos.png')
    plt.close()
    print("Se han generado los archivos correspondientes. ", time.time() - start_time, "segundos")


def graficas_personas():
    #   NUMERO DE COMPETIDORES ÚNICOS EN EL MUNDO / ESPAÑA POR AÑO
    #   formato:
    #   SELECT COUNT(*) FROM (
    #   SELECT DISTINCT competitionId, personId FROM wca_export.results
    #   INNER JOIN wca_export.competitions
    #   ON wca_export.results.competitionId=wca_export.competitions.id
    #   WHERE year = 2005
    #   ) AS x
    print("Comenzando el análisis de las estadísticas de competidores. ", time.time() - start_time, "segundos")
    year = 1982
    world_years = []
    world_competitors = []
    spain_competitors = []
    world_ncompetitors = 0
    spain_ncompetitors = 0
    while (actual_year>=year):
        sql = 'SELECT COUNT(*) FROM (SELECT DISTINCT competitionId, personId FROM wca_export.results INNER JOIN wca_export.competitions ON wca_export.results.competitionId=wca_export.competitions.id WHERE year ='
        sql += str(year)
        if (actual_year==year):
            sql += ' AND month<'
            sql += str(actual_month)
        sql += ') AS x'
        cursor.execute(sql)
        data = cursor.fetchone()
        print("Terminado el análisis de ",year, time.time() - start_time, "segundos")
        if (data[0]>0):
            world_years.append(str(year))
            world_competitors.append(data[0])
            world_ncompetitors += data[0]

        sql = sql.replace(') AS x','')
        sql += ' AND countryId=\'Spain\''
        sql += ') AS x'
        cursor.execute(sql)
        data = cursor.fetchone()
        if (data[0]>0 or year==2003 or year==1982):
            spain_competitors.append(data[0])
            spain_ncompetitors += data[0]
        year += 1
    print("Terminado el análisis de las estadísticas de competidores. ", time.time() - start_time, "segundos")

    #   GRÁFICAS PERSONAS
    y_pos = numpy.arange(len(world_years))

    fig_size = (12,9)
    plt.rcParams["figure.figsize"] = fig_size

    plt.text(7.03, max(spain_competitors), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, spain_competitors, align='center', alpha=0.5)
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de competidores')
    plt.title('Competidores anuales en España (hasta el 01/07/2018)')
    plt.savefig('competidores_anuales_s.png')
    plt.close()

    plt.text(7.03, max(world_competitors), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, world_competitors, align='center', alpha=0.5)
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de competidores')
    plt.title('Competidores anuales en el mundo (hasta el 01/07/2018)')
    plt.savefig('competidores_anuales_w.png')
    plt.close()

    plt.text(7.03, max(world_competitors)-(max(world_competitors)*0.07), 'Generado por Rodrigo Pueblas (@RGuitar96 2014NUNE05)',
        fontsize=10, color='gray',
        ha='right', va='bottom', alpha=0.5)
    plt.bar(y_pos, world_competitors, align='center', alpha=0.5, label = 'Mundial')
    plt.bar(y_pos, spain_competitors, align='center', alpha=0.5, label = 'España')
    plt.xticks(y_pos, world_years)
    plt.ylabel('Número de competidores')
    plt.title('Competidores anuales en el mundo y en España (hasta el 01/07/2018)')
    plt.legend(loc='upper left')
    plt.savefig('competidores_anuales_ws.png')
    plt.close()

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    plt.title('Estadísticas sobre el número de competidores anuales en España y en el mundo')
    percentages = []
    for i in range(0, len(world_years)):
        percentages.append(round(spain_competitors[i]/(world_competitors[i]/100),2))
    clust_data = numpy.array( [numpy.array(world_competitors),numpy.array(spain_competitors),numpy.array(percentages)] )
    rowlabel=("En el mundo", "En España", "En España sobre el total (%)")
    ax.table(cellText=clust_data, colLabels=numpy.array(world_years),rowLabels=rowlabel, 
            bbox=[0.1, 0.5, 1.0, 0.5],rowColours=['gray']*3, colColours=['gray']*17)
    plt.savefig('estadisticas_competidores.png')
    plt.close()
    print("Se han generado los archivos correspondientes. ", time.time() - start_time, "segundos")


def tabla_general():
    sql = 'SELECT COUNT(*) FROM wca_export.competitions'
    cursor.execute(sql)
    data = cursor.fetchone()
    world_ncompetitions = data[0]

    sql = 'SELECT COUNT(*) FROM wca_export.competitions WHERE countryId=\'Spain\''
    cursor.execute(sql)
    data = cursor.fetchone()
    spain_ncompetitions = data[0]

    sql = 'SELECT COUNT(*) FROM (SELECT DISTINCT countryId FROM wca_export.competitions) AS x'
    cursor.execute(sql)
    data = cursor.fetchone()
    world_ncountries_competitions = data[0]

    sql = 'SELECT COUNT(*) FROM (SELECT DISTINCT countryId FROM wca_export.persons) AS x'
    cursor.execute(sql)
    data = cursor.fetchone()
    world_ncountries_competitors = data[0]

    sql = 'SELECT COUNT(*) FROM wca_export.persons'
    cursor.execute(sql)
    data = cursor.fetchone()
    world_ncompetitors = data[0]

    sql = 'SELECT COUNT(*) FROM wca_export.persons WHERE countryId=\'Spain\''
    cursor.execute(sql)
    data = cursor.fetchone()
    spain_ncompetitors = data[0]

    sql = 'SELECT COUNT(*) FROM wca_export.results'
    cursor.execute(sql)
    data = cursor.fetchone()
    world_nresolutions = data[0]

    sql = 'SELECT COUNT(*) FROM wca_export.results INNER JOIN wca_export.competitions ON wca_export.results.competitionId=wca_export.competitions.id WHERE countryId=\'Spain\''
    cursor.execute(sql)
    data = cursor.fetchone()
    spain_nresolutions = data[0]

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    clust_data = numpy.array( [[world_ncompetitions],[spain_ncompetitions],[world_ncountries_competitions],[world_ncountries_competitors],[world_ncompetitors],[spain_ncompetitors],[world_nresolutions],[spain_nresolutions]] )
    rowlabel=("Número total de competiciones en el mundo", 
            "Número total de competiciones en España", 
            "Número total de países con competiciones", 
            "Número total de países con competidores",
            "Número total de competidores en el mundo",
            "Número total de competidores en España",
            "Número total de resoluciones en el mundo",
            "Número total de resoluciones en España")
    ax.table(cellText=clust_data, rowLabels=rowlabel, rowColours=['gray']*8, 
            bbox=[0.6, 0.3, 0.5, 0.5], loc='center')
    plt.show('estadisticas.png')
    plt.close()


start_time = time.time()


print("Conectando con la base de datos...")
now = datetime.datetime.now()
actual_year = now.year
actual_month = now.month

conexion = pymysql.connect(host='localhost', user='root', password='root', db='wca_export')
cursor = conexion.cursor()
print("Base de datos conectada. ", time.time() - start_time, "segundos")
print("")


print("***ESTADÍSTICAS CUBERAS ESPAÑOLAS***")
print("Por favor, elija la opción deseada introduciendo uno de los caracteres.")
print("a) ¿Cuántos campeonatos se han celebrado al año en España y en el mundo?")
print("b) ¿Cuántos resoluciones se han registrado al año en España y en el mundo?")
print("c) ¿Cuántos rondas por competidor (número de hojas de tiempos) han habido al año en España y en el mundo?")
print("d) ¿Cuántos nuevos competidores se han registrado al año en España y en el mundo?")
print("e) ¿Cuántos competidores únicos han participado al año en España y en el mundo?")
print("f) ¿Cuántos competidores han participado al año en España y en el mundo?")
print("g) Generar las tablas de estadísticas generales")
print("h) Generar todas las estadísticas y tablas (tardará alrededor de una hora)")
print("")
print("Introduzca cualquier otro caracter para salir.")

x = input()
start_time = time.time()

if (x=='a'):
    graficas_competiciones()
elif (x=='b'):
    graficas_resultados()
elif (x=='c'):
    graficas_rondas()
elif (x=='d'):
    graficas_nuevaspersonas()
elif (x=='e'):
    graficas_personasunicas()
elif (x=='f'):
    graficas_personas()
elif (x=='g'):
    tabla_general()
elif (x=='h'):
    graficas_competiciones()
    graficas_resultados()
    graficas_rondas()
    graficas_nuevaspersonas()
    graficas_personasunicas()
    graficas_personas()
    tabla_general()

print("Fin del programa.")