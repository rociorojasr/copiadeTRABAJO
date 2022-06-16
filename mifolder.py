{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ProyectoFinal.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JennyferRMcda/proyecto_grupo07/blob/main/mifolder.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!gdown --id 1Gu65mnJ_lxE0BdbkL1nTq5qaFJ1dJ9tq"
      ],
      "metadata": {
        "id": "rYbONqJsM3z2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "898da3c0-d029-4c38-fc58-08e80266bf63"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/gdown/cli.py:131: FutureWarning: Option `--id` was deprecated in version 4.3.1 and will be removed in 5.0. You don't need to pass it anymore to use a file ID.\n",
            "  category=FutureWarning,\n",
            "Downloading...\n",
            "From: https://drive.google.com/uc?id=1Gu65mnJ_lxE0BdbkL1nTq5qaFJ1dJ9tq\n",
            "To: /content/positivos_covid.csv\n",
            "100% 72.9M/72.9M [00:00<00:00, 192MB/s]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n"
      ],
      "metadata": {
        "id": "r5-4shCUS26K"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dataset = pd.read_csv(\"positivos_covid.csv\",sep=\";\")\n",
        "dataset"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "RPPh8KgXS9pm",
        "outputId": "d68489ca-dd1d-4e71-c241-f1413583372f"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         FECHA_CORTE DEPARTAMENTO         PROVINCIA              DISTRITO  \\\n",
              "0           20220523         LIMA              LIMA           JESUS MARIA   \n",
              "1           20220523        JUNIN          HUANCAYO              EL TAMBO   \n",
              "2           20220523         LIMA  EN INVESTIGACIÓN      EN INVESTIGACIÓN   \n",
              "3           20220523    CAJAMARCA              JAEN                PUCARA   \n",
              "4           20220523         LIMA              LIMA           JESUS MARIA   \n",
              "...              ...          ...               ...                   ...   \n",
              "1048570     20220523   SAN MARTIN             LAMAS              RUMISAPA   \n",
              "1048571     20220523       ANCASH            HUARAZ             PARIACOTO   \n",
              "1048572     20220523         LIMA              LIMA           SANTA ANITA   \n",
              "1048573     20220523         LIMA              LIMA           JESUS MARIA   \n",
              "1048574     20220523         LIMA              LIMA  SAN MARTIN DE PORRES   \n",
              "\n",
              "        METODODX  EDAD       SEXO  FECHA_RESULTADO  id_persona  \n",
              "0             AG  20.0   FEMENINO       20220110.0    13866369  \n",
              "1             AG  39.0  MASCULINO       20210429.0    13866556  \n",
              "2             AG  39.0   FEMENINO       20210702.0    13866581  \n",
              "3             AG  38.0   FEMENINO       20220126.0    13866692  \n",
              "4             AG  53.0   FEMENINO       20210831.0    13865937  \n",
              "...          ...   ...        ...              ...         ...  \n",
              "1048570       PR  24.0   FEMENINO       20200613.0    25563005  \n",
              "1048571       AG  24.0   FEMENINO       20220125.0    25563008  \n",
              "1048572      PCR  26.0  MASCULINO       20220117.0    25563014  \n",
              "1048573       AG  33.0   FEMENINO       20220119.0    25563040  \n",
              "1048574       PR  30.0   FEMENINO       20200805.0    25563057  \n",
              "\n",
              "[1048575 rows x 9 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-4ccbda6b-2d7a-41d9-ad24-e707ca900292\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>FECHA_CORTE</th>\n",
              "      <th>DEPARTAMENTO</th>\n",
              "      <th>PROVINCIA</th>\n",
              "      <th>DISTRITO</th>\n",
              "      <th>METODODX</th>\n",
              "      <th>EDAD</th>\n",
              "      <th>SEXO</th>\n",
              "      <th>FECHA_RESULTADO</th>\n",
              "      <th>id_persona</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>20220523</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>JESUS MARIA</td>\n",
              "      <td>AG</td>\n",
              "      <td>20.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>20220110.0</td>\n",
              "      <td>13866369</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>20220523</td>\n",
              "      <td>JUNIN</td>\n",
              "      <td>HUANCAYO</td>\n",
              "      <td>EL TAMBO</td>\n",
              "      <td>AG</td>\n",
              "      <td>39.0</td>\n",
              "      <td>MASCULINO</td>\n",
              "      <td>20210429.0</td>\n",
              "      <td>13866556</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>20220523</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>EN INVESTIGACIÓN</td>\n",
              "      <td>EN INVESTIGACIÓN</td>\n",
              "      <td>AG</td>\n",
              "      <td>39.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>20210702.0</td>\n",
              "      <td>13866581</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>20220523</td>\n",
              "      <td>CAJAMARCA</td>\n",
              "      <td>JAEN</td>\n",
              "      <td>PUCARA</td>\n",
              "      <td>AG</td>\n",
              "      <td>38.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>20220126.0</td>\n",
              "      <td>13866692</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>20220523</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>JESUS MARIA</td>\n",
              "      <td>AG</td>\n",
              "      <td>53.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>20210831.0</td>\n",
              "      <td>13865937</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048570</th>\n",
              "      <td>20220523</td>\n",
              "      <td>SAN MARTIN</td>\n",
              "      <td>LAMAS</td>\n",
              "      <td>RUMISAPA</td>\n",
              "      <td>PR</td>\n",
              "      <td>24.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>20200613.0</td>\n",
              "      <td>25563005</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048571</th>\n",
              "      <td>20220523</td>\n",
              "      <td>ANCASH</td>\n",
              "      <td>HUARAZ</td>\n",
              "      <td>PARIACOTO</td>\n",
              "      <td>AG</td>\n",
              "      <td>24.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>20220125.0</td>\n",
              "      <td>25563008</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048572</th>\n",
              "      <td>20220523</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>SANTA ANITA</td>\n",
              "      <td>PCR</td>\n",
              "      <td>26.0</td>\n",
              "      <td>MASCULINO</td>\n",
              "      <td>20220117.0</td>\n",
              "      <td>25563014</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048573</th>\n",
              "      <td>20220523</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>JESUS MARIA</td>\n",
              "      <td>AG</td>\n",
              "      <td>33.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>20220119.0</td>\n",
              "      <td>25563040</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048574</th>\n",
              "      <td>20220523</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>SAN MARTIN DE PORRES</td>\n",
              "      <td>PR</td>\n",
              "      <td>30.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>20200805.0</td>\n",
              "      <td>25563057</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1048575 rows × 9 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-4ccbda6b-2d7a-41d9-ad24-e707ca900292')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-4ccbda6b-2d7a-41d9-ad24-e707ca900292 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-4ccbda6b-2d7a-41d9-ad24-e707ca900292');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "filename = 'positivos_covid.csv'\n",
        "df = pd.read_csv(filename, sep=\";\", parse_dates=['FECHA_CORTE', 'FECHA_RESULTADO'])\n",
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "a8iAGvk5a1z4",
        "outputId": "293e7e32-ba3b-4f00-997b-742078bf3544"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        FECHA_CORTE DEPARTAMENTO         PROVINCIA              DISTRITO  \\\n",
              "0        2022-05-23         LIMA              LIMA           JESUS MARIA   \n",
              "1        2022-05-23        JUNIN          HUANCAYO              EL TAMBO   \n",
              "2        2022-05-23         LIMA  EN INVESTIGACIÓN      EN INVESTIGACIÓN   \n",
              "3        2022-05-23    CAJAMARCA              JAEN                PUCARA   \n",
              "4        2022-05-23         LIMA              LIMA           JESUS MARIA   \n",
              "...             ...          ...               ...                   ...   \n",
              "1048570  2022-05-23   SAN MARTIN             LAMAS              RUMISAPA   \n",
              "1048571  2022-05-23       ANCASH            HUARAZ             PARIACOTO   \n",
              "1048572  2022-05-23         LIMA              LIMA           SANTA ANITA   \n",
              "1048573  2022-05-23         LIMA              LIMA           JESUS MARIA   \n",
              "1048574  2022-05-23         LIMA              LIMA  SAN MARTIN DE PORRES   \n",
              "\n",
              "        METODODX  EDAD       SEXO FECHA_RESULTADO  id_persona  \n",
              "0             AG  20.0   FEMENINO      2022-01-10    13866369  \n",
              "1             AG  39.0  MASCULINO      2021-04-29    13866556  \n",
              "2             AG  39.0   FEMENINO      2021-07-02    13866581  \n",
              "3             AG  38.0   FEMENINO      2022-01-26    13866692  \n",
              "4             AG  53.0   FEMENINO      2021-08-31    13865937  \n",
              "...          ...   ...        ...             ...         ...  \n",
              "1048570       PR  24.0   FEMENINO      2020-06-13    25563005  \n",
              "1048571       AG  24.0   FEMENINO      2022-01-25    25563008  \n",
              "1048572      PCR  26.0  MASCULINO      2022-01-17    25563014  \n",
              "1048573       AG  33.0   FEMENINO      2022-01-19    25563040  \n",
              "1048574       PR  30.0   FEMENINO      2020-08-05    25563057  \n",
              "\n",
              "[1048575 rows x 9 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-8ff0343d-7925-432d-8f51-df8994e40706\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>FECHA_CORTE</th>\n",
              "      <th>DEPARTAMENTO</th>\n",
              "      <th>PROVINCIA</th>\n",
              "      <th>DISTRITO</th>\n",
              "      <th>METODODX</th>\n",
              "      <th>EDAD</th>\n",
              "      <th>SEXO</th>\n",
              "      <th>FECHA_RESULTADO</th>\n",
              "      <th>id_persona</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2022-05-23</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>JESUS MARIA</td>\n",
              "      <td>AG</td>\n",
              "      <td>20.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>2022-01-10</td>\n",
              "      <td>13866369</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2022-05-23</td>\n",
              "      <td>JUNIN</td>\n",
              "      <td>HUANCAYO</td>\n",
              "      <td>EL TAMBO</td>\n",
              "      <td>AG</td>\n",
              "      <td>39.0</td>\n",
              "      <td>MASCULINO</td>\n",
              "      <td>2021-04-29</td>\n",
              "      <td>13866556</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2022-05-23</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>EN INVESTIGACIÓN</td>\n",
              "      <td>EN INVESTIGACIÓN</td>\n",
              "      <td>AG</td>\n",
              "      <td>39.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>2021-07-02</td>\n",
              "      <td>13866581</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2022-05-23</td>\n",
              "      <td>CAJAMARCA</td>\n",
              "      <td>JAEN</td>\n",
              "      <td>PUCARA</td>\n",
              "      <td>AG</td>\n",
              "      <td>38.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>2022-01-26</td>\n",
              "      <td>13866692</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2022-05-23</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>JESUS MARIA</td>\n",
              "      <td>AG</td>\n",
              "      <td>53.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>2021-08-31</td>\n",
              "      <td>13865937</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048570</th>\n",
              "      <td>2022-05-23</td>\n",
              "      <td>SAN MARTIN</td>\n",
              "      <td>LAMAS</td>\n",
              "      <td>RUMISAPA</td>\n",
              "      <td>PR</td>\n",
              "      <td>24.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>2020-06-13</td>\n",
              "      <td>25563005</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048571</th>\n",
              "      <td>2022-05-23</td>\n",
              "      <td>ANCASH</td>\n",
              "      <td>HUARAZ</td>\n",
              "      <td>PARIACOTO</td>\n",
              "      <td>AG</td>\n",
              "      <td>24.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>2022-01-25</td>\n",
              "      <td>25563008</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048572</th>\n",
              "      <td>2022-05-23</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>SANTA ANITA</td>\n",
              "      <td>PCR</td>\n",
              "      <td>26.0</td>\n",
              "      <td>MASCULINO</td>\n",
              "      <td>2022-01-17</td>\n",
              "      <td>25563014</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048573</th>\n",
              "      <td>2022-05-23</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>JESUS MARIA</td>\n",
              "      <td>AG</td>\n",
              "      <td>33.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>2022-01-19</td>\n",
              "      <td>25563040</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048574</th>\n",
              "      <td>2022-05-23</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>LIMA</td>\n",
              "      <td>SAN MARTIN DE PORRES</td>\n",
              "      <td>PR</td>\n",
              "      <td>30.0</td>\n",
              "      <td>FEMENINO</td>\n",
              "      <td>2020-08-05</td>\n",
              "      <td>25563057</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1048575 rows × 9 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-8ff0343d-7925-432d-8f51-df8994e40706')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-8ff0343d-7925-432d-8f51-df8994e40706 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-8ff0343d-7925-432d-8f51-df8994e40706');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "A= dataset.iloc[0:,7]\n",
        "A"
      ],
      "metadata": {
        "id": "ooffRadGJFL4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8bbcb2e4-3ee6-4271-aeb7-eb8058dc77a6"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0          20220110.0\n",
              "1          20210429.0\n",
              "2          20210702.0\n",
              "3          20220126.0\n",
              "4          20210831.0\n",
              "              ...    \n",
              "1048570    20200613.0\n",
              "1048571    20220125.0\n",
              "1048572    20220117.0\n",
              "1048573    20220119.0\n",
              "1048574    20200805.0\n",
              "Name: FECHA_RESULTADO, Length: 1048575, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dataset.SEXO"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b7EnpPLrNlRs",
        "outputId": "145a7a55-cfc1-425d-b7ca-5d851e2c6487"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0           FEMENINO\n",
              "1          MASCULINO\n",
              "2           FEMENINO\n",
              "3           FEMENINO\n",
              "4           FEMENINO\n",
              "             ...    \n",
              "1048570     FEMENINO\n",
              "1048571     FEMENINO\n",
              "1048572    MASCULINO\n",
              "1048573     FEMENINO\n",
              "1048574     FEMENINO\n",
              "Name: SEXO, Length: 1048575, dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dataset.DEPARTAMENTO.hist(figsize=(20,10))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 609
        },
        "id": "uDZIFTfpLvYu",
        "outputId": "255cceaf-1037-4ee0-b5ff-432ff471bae6"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7ff7265c1050>"
            ]
          },
          "metadata": {},
          "execution_count": 7
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1440x720 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAABJcAAAI/CAYAAADKljhRAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzde7RkVWEm8G9r+yC2AorpuBpW2kQ0QdoXvYA8XNOtiI2awWTUkcUoOETiiImukBlaJ0ajMsHJcowYH2GUBSQmLeNoIIAhDNqZmAkKRBQfMbRIxu4gRECcRny07vmj9pXiUvfRm6JvHfn91rqrq/Y5dc5Xp845Vffrqlul1hoAAAAA6PGAlQ4AAAAAwHAplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOi2aqUDTNsBBxxQ161bt9IxpuKOO+7Iwx72sJWOsSQ5p2soOZPhZJVzuoaSMxlOVjmnbyhZ5ZyuoeRMhpNVzukaSs5kOFnlnL6hZJVz77v66qu/Xmt99MSJtdYfqZ/DDjus/qj4+Mc/vtIRlkXO6RpKzlqHk1XO6RpKzlqHk1XO6RtKVjmnayg5ax1OVjmnayg5ax1OVjmnbyhZ5dz7klxVF+hifCwOAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACg26qVDsDCrt15e07ccvFKx1jSqet3329y3nDGc6eUBgAAAH40eOcSAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdllUulVJuKKVcW0q5ppRyVRt7ZCnlslLKde3f/dt4KaWcWUrZXkr5bCnlaWPLOaHNf10p5YSx8cPa8re325bF1gEAAADAbNiTdy5tqrU+pda6oV3fkuTyWuvBSS5v15PkmCQHt5+Tk7wnGRVFSd6Q5Igkhyd5w1hZ9J4kLx+73eYl1gEAAADADLg3H4s7Nsm57fK5SZ4/Nn5eHbkiyX6llMckeXaSy2qtt9Zab0tyWZLNbdojaq1X1FprkvPmLWvSOgAAAACYAcstl2qSvyqlXF1KObmNram13tgufy3JmnZ5bZKvjt12RxtbbHzHhPHF1gEAAADADCijNwstMVMpa2utO0spP57RO45+PcmFtdb9xua5rda6fynloiRn1Fo/0cYvT3Jako1JHlprfUsbf32SO5Nsa/Mf1cafnuS0WuvzSinfmLSOCflOzugjeFmzZs1hW7du7dgUs+fmW2/PTXeudIqlrdkn95uc69fuO50wi9i1a1dWr159n69nGoaSVc7pGkrOZDhZ5Zy+oWSVc7qGkjMZTlY5p2soOZPhZJVz+oaSVc69b9OmTVeP/amku1m1nAXUWne2f28upXwko7+ZdFMp5TG11hvbR9tubrPvTHLQ2M0PbGM7MyqYxse3tfEDJ8yfRdYxP99ZSc5Kkg0bNtSNGzdOmm1w3vmBC/K2a5f1EK2oU9fvvt/kvOH4jdMJs4ht27ZlKPvwULLKOV1DyZkMJ6uc0zeUrHJO11ByJsPJKud0DSVnMpysck7fULLKOVuW/FhcKeVhpZSHz11OcnSSzyW5MMncN76dkOSCdvnCJC9t3xp3ZJLb20fbLk1ydCll//aHvI9Ocmmb9s1SypHtW+JeOm9Zk9YBAAAAwAxYzts41iT5yKj3yaokf1pr/ctSypVJzi+lnJTkn5K8qM1/SZLnJNme5FtJXpYktdZbSylvTnJlm+9NtdZb2+VXJjknyT5JPtp+kuSMBdYBAAAAwAxYslyqtV6f5MkTxm9J8swJ4zXJKQss6+wkZ08YvyrJoctdBwAAAACzYbnfFgcAAAAA96BcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAui27XCqlPLCU8ulSykXt+mNLKZ8spWwvpXywlPLgNv6Qdn17m75ubBmvbeNfKqU8e2x8cxvbXkrZMjY+cR0AAAAAzIY9eefSq5N8cez6W5O8vdb6uCS3JTmpjZ+U5LY2/vY2X0ophyR5cZInJtmc5N2tsHpgknclOSbJIUmOa/Mutg4AAAAAZsCyyqVSyoFJnpvkfe16SfKMJB9qs5yb5Pnt8rHtetr0Z7b5j02ytdb6nVrrV5JsT3J4+9lea72+1vrdJFuTHLvEOgAAAACYAct959IfJPlPSX7Qrj8qyTdqrbvb9R1J1rbLa5N8NUna9Nvb/D8cn3ebhcYXWwcAAAAAM6DUWhefoZTnJXlOrfWVpZSNSX4ryYlJrmgfV0sp5aAkH621HlpK+VySzbXWHW3al5MckeSN7TZ/0sbfn+SjbTWba62/2sZfMm/+e6xjQsaTk5ycJGvWrDls69atXRtj1tx86+256c6VTrG0NfvkfpNz/dp9pxNmEbt27crq1avv8/VMw1CyyjldQ8mZDCernNM3lKxyTtdQcibDySrndA0lZzKcrHJO31Cyyrn3bdq06epa64ZJ01Yt4/a/kORfl1Kek+ShSR6R5B1J9iulrGrvLDowyc42/84kByXZUUpZlWTfJLeMjc8Zv82k8VsWWcfd1FrPSnJWkmzYsKFu3LhxGXdr9r3zAxfkbdcu5yFaWaeu332/yXnD8RunE2YR27Zty1D24aFklXO6hpIzGU5WOadvKFnlnK6h5EyGk1XO6RpKzmQ4WeWcvqFklXO2LPmxuFrra2utB9Za12X0B7k/Vms9PsnHk7ygzXZCkgva5Qvb9bTpH6ujt0ddmOTF7dvkHpvk4CSfSnJlkoPbN8M9uK3jwnabhdYBAAAAwAzYk2+Lm++0JL9ZStme0d9Hen8bf3+SR7Xx30yyJUlqrZ9Pcn6SLyT5yySn1Fq/396V9Kokl2b0bXTnt3kXWwcAAAAAM2CPPiNUa92WZFu7fH1G3/Q2f55vJ3nhArc/PcnpE8YvSXLJhPGJ6wAAAABgNtybdy4BAAAAcD+nXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALotWS6VUh5aSvlUKeUzpZTPl1J+t40/tpTyyVLK9lLKB0spD27jD2nXt7fp68aW9do2/qVSyrPHxje3se2llC1j4xPXAQAAAMBsWM47l76T5Bm11icneUqSzaWUI5O8Ncnba62PS3JbkpPa/Cclua2Nv73Nl1LKIUlenOSJSTYneXcp5YGllAcmeVeSY5IckuS4Nm8WWQcAAAAAM2DJcqmO7GpXH9R+apJnJPlQGz83yfPb5WPb9bTpzyyllDa+tdb6nVrrV5JsT3J4+9lea72+1vrdJFuTHNtus9A6AAAAAJgBy/qbS+0dRtckuTnJZUm+nOQbtdbdbZYdSda2y2uTfDVJ2vTbkzxqfHzebRYaf9Qi6wAAAABgBpRa6/JnLmW/JB9J8vok57SPq6WUclCSj9ZaDy2lfC7J5lrrjjbty0mOSPLGJFfUWv+kjb8/yUfbojfXWn+1jb9k3vz3WMeEXCcnOTlJ1qxZc9jWrVv3ZBvMrJtvvT033bnSKZa2Zp/cb3KuX7vvdMIsYteuXVm9evV9vp5pGEpWOadrKDmT4WSVc/qGklXO6RpKzmQ4WeWcrqHkTIaTVc7pG0pWOfe+TZs2XV1r3TBp2qo9WVCt9RullI8n+bkk+5VSVrV3Fh2YZGebbWeSg5LsKKWsSrJvklvGxueM32bS+C2LrGN+rrOSnJUkGzZsqBs3btyTuzWz3vmBC/K2a/foIVoRp67ffb/JecPxG6cTZhHbtm3LUPbhoWSVc7qGkjMZTlY5p28oWeWcrqHkTIaTVc7pGkrOZDhZ5Zy+oWSVc7Ys59viHt3esZRSyj5JnpXki0k+nuQFbbYTklzQLl/YrqdN/1gdvT3qwiQvbt8m99gkByf5VJIrkxzcvhnuwRn90e8L220WWgcAAAAAM2A5b+N4TJJz27e6PSDJ+bXWi0opX0iytZTyliSfTvL+Nv/7k/xxKWV7klszKotSa/18KeX8JF9IsjvJKbXW7ydJKeVVSS5N8sAkZ9daP9+WddoC6wAAAABgBixZLtVaP5vkqRPGr8/om97mj387yQsXWNbpSU6fMH5JkkuWuw4AAAAAZsOyvi0OAAAAACZRLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAtyXLpVLKQaWUj5dSvlBK+Xwp5dVt/JGllMtKKde1f/dv46WUcmYpZXsp5bOllKeNLeuENv91pZQTxsYPK6Vc225zZimlLLYOAAAAAGbDct65tDvJqbXWQ5IcmeSUUsohSbYkubzWenCSy9v1JDkmycHt5+Qk70lGRVGSNyQ5IsnhSd4wVha9J8nLx263uY0vtA4AAAAAZsCS5VKt9cZa69+3y/8vyReTrE1ybJJz22znJnl+u3xskvPqyBVJ9iulPCbJs5NcVmu9tdZ6W5LLkmxu0x5Ra72i1lqTnDdvWZPWAQAAAMAM2KO/uVRKWZfkqUk+mWRNrfXGNulrSda0y2uTfHXsZjva2GLjOyaMZ5F1AAAAADADyujNQsuYsZTVSf46yem11g+XUr5Ra91vbPpttdb9SykXJTmj1vqJNn55ktOSbEzy0FrrW9r465PcmWRbm/+oNv70JKfVWp+30DomZDs5o4/gZc2aNYdt3bp1T7fDTLr51ttz050rnWJpa/bJ/Sbn+rX7TifMInbt2pXVq1ff5+uZhqFklXO6hpIzGU5WOadvKFnlnK6h5EyGk1XO6RpKzmQ4WeWcvqFklXPv27Rp09W11g2Tpq1azgJKKQ9K8j+TfKDW+uE2fFMp5TG11hvbR9tubuM7kxw0dvMD29jOjAqm8fFtbfzACfMvto67qbWeleSsJNmwYUPduHHjpNkG550fuCBvu3ZZD9GKOnX97vtNzhuO3zidMIvYtm1bhrIPDyWrnNM1lJzJcLLKOX1DySrndA0lZzKcrHJO11ByJsPJKuf0DSWrnLNlOd8WV5K8P8kXa63/bWzShUnmvvHthCQXjI2/tH1r3JFJbm8fbbs0ydGllP3bH/I+Osmlbdo3SylHtnW9dN6yJq0DAAAAgBmwnLdx/EKSlyS5tpRyTRt7XZIzkpxfSjkpyT8leVGbdkmS5yTZnuRbSV6WJLXWW0spb05yZZvvTbXWW9vlVyY5J8k+ST7afrLIOgAAAACYAUuWS+1vJ5UFJj9zwvw1ySkLLOvsJGdPGL8qyaETxm+ZtA4AAAAAZsMefVscAAAAAIxTLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0G3VSgcAuDfWbbl4yXlOXb87Jy5jvpX2o5TzhjOeu5fSAAAAK807lwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbsolAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6LZkuVRKObuUcnMp5XNjY48spVxWSrmu/bt/Gy+llDNLKdtLKZ8tpTxt7DYntPmvK6WcMDZ+WCnl2nabM0spZbF1AAAAADA7lvPOpXOSbJ43tiXJ5bXWg5Nc3q4nyTFJDm4/Jyd5TzIqipK8IckRSQ5P8oaxsug9SV4+drvNS6wDAAAAgBmxZLlUa/3fSW6dN3xsknPb5XOTPH9s/Lw6ckWS/Uopj0ny7CSX1VpvrbXeluSyJJvbtEfUWq+otdYk581b1qR1AAAAADAjev/m0ppa643t8teSrGmX1yb56th8O9rYYuM7Jowvtg4AAAAAZkQZvWFoiZlKWZfkolrroe36N2qt+41Nv63Wun8p5aIkZ9RaP9HGL09yWpKNSR5aa31LG399kjuTbGvzH9XGn57ktFrr8xZaxwL5Ts7oY3hZs2bNYVu3bt2jjTCrbr719tx050qnWNqafXK/ybl+7b7TCbOIXbt2ZfXq1ff5eqZhFrJeu/P2Jee5P+2je8Nycu6NY2U5ZmEfXQ45p28oWeWcrqHkTIaTVc7pGkrOZDhZ5Zy+oWSVc+/btGnT1bXWDZOmrepc5k2llMfUWm9sH227uY3vTHLQ2HwHtrGdGRVM4+Pb2viBE+ZfbB33UGs9K8lZSbJhw4a6cePGhWYdlHd+4IK87dreh2jvOXX97vtNzhuO3zidMIvYtm1bhrIPz0LWE7dcvOQ896d9dG9YTs69cawsxyzso8sh5/QNJauc0zWUnMlwsso5XUPJmQwnq5zTN5Sscs6W3o/FXZhk7hvfTkhywdj4S9u3xh2Z5Pb20bZLkxxdStm//SHvo5Nc2qZ9s5RyZPuWuJfOW9akdQAAAAAwI5b8L/JSyp9l9K6jA0opOzL61rczkpxfSjkpyT8leVGb/ZIkz0myPcm3krwsSWqtt5ZS3pzkyjbfm2qtc38k/JUZfSPdPkk+2n6yyDoAAAAAmBFLlku11uMWmPTMCfPWJKcssJyzk5w9YfyqJIdOGL9l0joAAAAAmB29H4sDAAAAAOUSAAAAAP2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0W7XSAQAAYFas23LxXlnPqet358S9tK57Y1Zy3nDGc1c6AgCL8M4lAAAAALoplwAAAADoplwCAAAAoJtyCQAAAIBuyiUAAAAAuimXAAAAAOimXAIAAACgm3IJAAAAgG7KJQAAAAC6KZcAAAAA6KZcAgAAAKCbcgkAAACAbqtWOgAAwP3VtTtvz4lbLl7pGEs6df1uOQGABXnnEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQbdVKB4AhWbfl4vt8Haeu350T98J6pmFIWQEAALhveOcSAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdVq10AAAAAIZl3ZaLVzpCkuTU9btz4oxkWczeynnDGc+9z9cBk3jnEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0G3VSgcAAABYzLotFy86/dT1u3PiEvPMgqHkTIaVFVh53rkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANDNH/QGYOqW+sOre8tQ/hipnNM3lKynrl/pBAAA9553LgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3VatdAAAAADg3lu35eJ7vYxT1+/OiVNYzn1tKDnP2fywlY6wV3jnEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAN+USAAAAAN2USwAAAAB0Uy4BAAAA0E25BAAAAEA35RIAAAAA3ZRLAAAAAHRTLgEAAADQTbkEAAAAQDflEgAAAADdlEsAAAAAdFMuAQAAANBNuQQAAABAt5kvl0opm0spXyqlbC+lbFnpPAAAAADcZabLpVLKA5O8K8kxSQ5Jclwp5ZCVTQUAAADAnJkul5IcnmR7rfX6Wut3k2xNcuwKZwIAAACgmXdS7TYAAB8QSURBVPVyaW2Sr45d39HGAAAAAJgBpda60hkWVEp5QZLNtdZfbddfkuSIWuur5s13cpKT29UnJPnSXg163zkgyddXOsQyyDldQ8mZDCernNM1lJzJcLLKOX1DySrndA0lZzKcrHJO11ByJsPJKuf0DSWrnHvfT9ZaHz1pwqq9nWQP7Uxy0Nj1A9vY3dRaz0py1t4KtbeUUq6qtW5Y6RxLkXO6hpIzGU5WOadrKDmT4WSVc/qGklXO6RpKzmQ4WeWcrqHkTIaTVc7pG0pWOWfLrH8s7sokB5dSHltKeXCSFye5cIUzAQAAANDM9DuXaq27SymvSnJpkgcmObvW+vkVjgUAAABAM9PlUpLUWi9JcslK51ghQ/mon5zTNZScyXCyyjldQ8mZDCernNM3lKxyTtdQcibDySrndA0lZzKcrHJO31CyyjlDZvoPegMAAAAw22b9by4BAAAAMMtqrX724k+SXRPG3pjkt9rlc5J8K8nDx6b/QZKa5ICxsee3sZ+Zdr4kG5NcNG/8nCQvaJe3JblqbNqGJNva5R/eNsmJSX6Q5Elj834uybp2+SeSbE3y5SRXZ/Txx8e3aa9J8u0k+47ddlKua5JsnZC1axsmWZfkzrbcLyQ5L8mD2rQHJTkjyXVJ/j7J3yU5Zuy2T2nLO27C/Tp5iW36vCSfTvKZtt5fG5vvpW27XdvmmdtXSpLfbnn+McnHkzxx3jrudh8n3L/3ZlQyL+cx/1LLd2WSp4zNd8Pcdm3r+pOxaauS/MuEZf95kism7H+/leQfWr4rk/z6vd1HxvJvWGCfn3gsJfnFJJ9qef4hycl7cBx9v92HzyX5H0l+bPz4vzfbe2x/3pnkAYtkWOqxH9+3Nya5vU2b+zmqTTswyQVtP7s+yR8mecjYMf6HC23refvG+Db527lsbR+5pV1/y9hyDkjyvQnLv9sxn9Hf47tm3s/Xk3ywTX9w217b2324IMmBY7evSd42bx9844THc3ydJ7bH9ZNJbk2yY/w2mXeez8L7ak3yS2NjFyXZOH/bTdpnkhyT5Kr2WH46ydvGHvPfaY/n1zLah38xyRFJPpvReWzuuDxjXs7VSf4odx1v29rt1iX53Lx535h2Llrg2H3ppGNv/rKyjOMsE46npTJldDztzF376gFJbhib94lJPpbRcXZdku+kvZt7wvoXPd7mPzaLHAvXtvtxbZJjJ9y/uZ8tC50Hkrwrdx3Dd47dZu7ccY9za9suO9t8Nck32n0ePzcttE/cJ89NE7bVpNdG+2Z0ntqe0T55XtoxlD0/n/3bsctfG9se12R0jhg/z305yTuSPHixzMv5Gb9fSR6f0XPY3GuI85OsWe5+1rHuSc8BNcmvj83zh0lOXOo4HjuGvpfkFfPW8+/bPvDZtj8cO3YMvmCpx3ls2qMWeYx+fIF1T3wducz7OrfP/3WSz7f81yQ5YsI884+LbVngdfC8+eZy7PFz29g2/Eqb9pkkz0zyn8e2y/i54zcyOtZPb4/DOW0bPqSN/05G56FlP8ZJXp72XNquP6Jt658aP9/k7vv5G3P354a5/Xp8nhPbdjlqwv46/3XQNUm+mHnPDbnrNffmdv30JG8dm/6TGb1m2W/esq5J8qE2T235555/rsro/Dj3e8wNSV7S9o0vtuVdOXYf/iXJjRk9f3y7bc/x33nmvxY4ce5xb9upZvQaYi7Xo9oyP9Eyz50rvpbkM+PHVe5+Xv9Bkg8nOaTN85o2dl0Wft0+93x0TZIzJ+y748u/ri3/jnnHwI0t7zVtmfOP92+36Z9uy/iHtq32Hbsvb2jb4Zdz12u1O9o2ODB3/e719YzO+XdktA8escB+cEKSP5uX44CW4yFZeF94Y+6+386dj76fu85HX8zo+PhOxs7hc7dt+e/IEr+D5q7j9jNtOT8/dr4Yf16/Jne9lpp4np3FH+9cmk3bkxybJKWUByR5RkY79bjjMjrwjtu70X7ox0spxyxjvh0ZPRHeTSmlJPlIRk/GP11rPSzJazM6SJPR/boyya8stOBSys9m9Ivl00spD5s3+d5swy/XWp+SZH1GJ7YXtfE3J3lMkkNrrU/L6Inw4ROW945F7tek+/GgjD6H+0u11icneWpGJ7+0bfyaJEfXWtcnOTKjF81JckqSn0/y5Frr45P8XpILSykPXeI+zt2/JyU5pN2P5Ti+5Xt3kt9fYJ47khxaStmnXX9W5m33Usp+SQ5Lsm8p5afGxl/R5j+85XtmklfnXuwjy3SPbVRK+Ykkf5rRC6yfyegX4F8rpTx3mcu8s9b6lFrroUm+m+QVHbkmbu+2P/9ykq8m+VeL3H6xx37+vp0kf9Myz/38r3acfjjJn9daD05ycJJ9kvzXjvszvk0OzOgF83EZPeZfSbI7yfj2fWFGL/h/aNIxX2v9/njujEqXOzM6XpPkv2R0nD6h3Yc/T/Lhdt+S0YuEXymlHDApdFtncs/zzFEZlcYXJvnNjF5kLGShfXXi+XEppZRDM/pF6d/VWg/J6Beb7W09X8hofzsyoxc4WzLal9+b5JW11u9ltM3/MckLx7ZDkrwvoxe6B7fj7WUZvShbKs+kY7csfqs9Os56j6fvZ/SCbP5698nocTuj1vqEJE/OaL965YR5l3u8Lcemtn1ekOTMsfE75x17Z4xNu9t5oNZ6SlvGc9KO5/bzoYXOrc3b2+3uSPJrGR0TJXdty3vsE/fxc9NyvD/J9bXWx9Vafzqj88T7xqbvyfnsg2PniPfObY92/Xu5+3nu8RkVrafvYd4Ftft+cZL31FoPbq8h3p3k0W36NPezOZOeA25O8ur2DczzMy51HL8wo1/Ex58rD8zoHPaLtdYnZbQffLYnbK31lkUeo38zYd1LvY5c8L42z8rol+Mjkjyt5T8qo8dgfJ5J58pk+a+Dv5KO57Yx/7Ftg9ckeW+t9fSx7TJ+7jgz9zT/HPjw7Nlj/L4kB5VSjmrX35TRlytdP36+yQLn+3n79QPnTb42o28Bn3NcRr9sjzu+5fyFJG+d91jO37/fkuT5Y8/Z70jy+lrrN8aX1X5e0Ma+ndFr4aPac9A5Gf3nxdy56kFJfjejX+R/NsnrkhxSSnlSmz73nzv711ofmtGxcOGEx3Ah303yf5P8XLufhye5KcnTkryunY+ekdH2feQi5/VvJflgko+VUh7dtsk3k/zpIq/bN41tj99YIN/cMXhwW/4+bflz/iij8vEpac8NE3yw1vrUtowftPtyyrx5dmT0HycPT/KEjP5D4hMZnZffnNFjtD2jovCnMnpdN3eczt8PPpLkWaWUHxtb/guS/EWt9Tvt+qR94W7mzkcZvZ58b5J3ZlQ2vyLJdfPP4e1+/XJGj8WNWfx30Lnj9skZnbN+b2za+PP6U2qt503zPLs3KJdm09aM/pctGf0P3N9m9ItXkqSUsjqjF+En5e4n5r3p97O8X4ouSvLEUsoT5o1vSvK9Wut75wZqrZ+ptf5NKeWnM3ph99tZvDw7LskfJ/mrtIN4zL3ehrXW72f0P+pr20nq5Rn9L9h32vSbaq3nt+WVjJ6U35vRE+054/cryd8scj8enrvevZFa63dqrV9q016bUZP+z2PT/nubdlqSV9Vav9Wm/VWS/5Pk+OXcx1rr7jb/4xbJNsnfJVm7yPRLctcLqeOS/Nm86b+S5C8yeozGc70uyX+otX6zXd+Q5J/v5T6yqEW20SnJ/2/vzKPtrqo7/tkJg2FIJCkIYUgQsBAaCCSCAoEHgqgoLIqQhFAaKMvKomgZQi3qIhYoKIroIiilaRgagSUBZRAUgSBTDZA+IGFIeGQog1lhsAESSMjb/WPv373nnvv7/e7v3vciaXu+a7317v3d8zvDPnvvs88++5zDtao6z8t9HTgPm6i3i4don8YhYnp3YYbpTyhoe4W+r/F2i7IPA95T1ZnBe2cBJ3sZbcPfG4y1a6K3YSbm5FkhIuM86QSaHTZlMp/J4XXYJHy+y+0pwFled7wt73vbwPTCv3i78jDJ08RlDsIMCIBeVX22oL1lvPoU8N8ickRB2UU4D7hYVZ+HWr/cgPX5amCdqj4HfB9bdZ3v6R4O2vQj3KgN6rk/8C1V7fX0i1X1rgr1aZBdVV2pqtdVeK8TOWtHnq4AzhKR+PKSE4FHXGfiOvT9gnK7aCFvHWAw8Fab77TSu1CsWxugqjdj/LyOOi2beIL1NDZVgYjsik1cLwwe/xMwznk1bE9VfVaEIj13ajRB6QtOBB5T1TuyB6o6R1Xn+9cu+pHPSsaAFcB92Op+jFZyPAk4B7OJdvBn2wBvY1HvqOo7qrq4r/XPQV7ZhXakfy1ra5bnb7zuY/391zOeDtLEcpGhqh28CniuL2Obo4oOiHEFxsvZfG8IbfSxqio2mb7C6/8Z6k6KUN8UXRDVRZ2v4zQPAfuJyMbOr7tikRp52AJzjK+DBpt7CuZI+Iiqrva2TheRL2CRI7OKCOPYBHNGfMq/7+f1GuHfhwBXBDz9B8zJMdW/70uzrnuINnQdzTbzcuBlVX3Un/0lMBtz9FXR62di9FoMHOk/d8I7efmvw3RZ23C9rdic4G+jn5/BFrJuz2w14B7M8X86MAtY4ePMclWdoaqvFvDBSiwa8UtB/hNpnou0i30wOt6XPYh0+C4Yrz+PjZmFc9AIVeyBP5We7Rck59KGiYXA1iKyFfUtViGOAe5R1YXAGyIy9k9dQUzA1ojIoS3S9WJRDudHz/8CC2HOw0SszQ8Bfy4iRVE/EzzdjTQbY32moa807o8puF2BZYHjI8YBmCIfRvMqVSlU9U1sFX2piNwoIpPd0w0FdBKRwcDmqvpS9NMT2HaPlm10o/kzmFJvB5/Doj+KcBMw0em3F7Z1KETmcKr1m7dny6g9/cEjrVBEoz1zyg5pWwk+qf087dM4REzvjH63AUd5dEGMVn0f8naG8SLSHfztQg4dXAaW0LnD7FhsRe1hLErm88BvsaiHNRjv7IgZMa9G75bJPJhh+QG2wgTFchv35XRgsogMyclzAmYUHwz8RES6sUnuU1ho9aG4UVPQ3la8ejHmeGoHebJxDNafHwde9T7/KRadOBZfNfN6Ho5NCkI67gl0B4ZdJRTIboxZGV/RePtrW3LWgTwtw/jsr6LneeUqsIW3J0QVeauKB0RkPmb4hn0+KJK9CTnvttK7YV2L5CNENzaReqaIJ9bj2FQFo4j40T93x/m0oc+KUKTnltG3hYEQZeMZ9C+fQfkY8F3gXBGpRZK0kmPXydup6lzMMZLx6FPYZHixiMwUkS9Fr14W9kMnDSkpuxVNIaetnmfG85diDvm7ROQqETkkJ02sKzNUtYOhbhd1OrZBNR0QI9OBe2EROdJuH6vq08CvsUn1maq6xl8J9U2Rcynk64ERXys29h+J8evtOe/PEpGnsbH2wkAfHAAsVtUeLGLmKK/rr7CJ+nU0R6LOCngxc5ANwMb/0Ga9n/quhI1pjqb6I6YzPgJsjkVCZ/kOwnTdqAJ6xNgYcx79q4g86OVvTD0KFNrT6/Mwet7keYxwmyOPdx4I6l20uBZjIPBtl+VxmHN1QvC9DJkt9Ass6i+0hTbH7Mqzo3dewpwqv8Qi6BZGcprLBxitJgKIyHAsGvX+IN88XmiFbSnXN2O83GWYo2mbkjloNuY/jzkNw0WUXaKxazyt9ewGheRc2nBxKyYY+9Mc9RIy6k30/9Y4rfj8IqpNin4GfEpEdq5Y/iRs33kv5q0/Pk7gKyivq+oybMDbR0SGRsk6peEuriiXA6/5wFqpzv75BZr7pJSmqnoa5uiZi+3b/bcKZbZTp7CNWfseAe5S1btb1c8xS0QWY4PJ9KJCnV4jvbxwIokPJrsBD7vRu1Zsi0+7aMkj7eTjn/tTlgY5jZ/ABpoZ0e8d0VssJPwL2PaNlZjj7simXFr3fR5vx9tIeiq0s6qugDpNrsTCyGdgIeUrsKiRldj2pCMwub05fLmVzIvI3ti2gVN8tbUynJbXY2dWNJWJTT4+gRk5h2FnVzyOGVOvYBEC4cQ2LL+UV1X1d17WQXG18qpa0oywz2cDk7zMqzGDKJsQfBF4wFd5Z2PbCOLtClXLrUrnWgg6xr/tIk+eqtbpEmyVuW17pw15q4pD1bb2jQaulHr0X7wtLuT9Snq3Dd2a0fIcbBV0BiU8sZ7Gpv5Cf+uzDwXrgc+gZGxz58LvaS8CIYy2qeXnk/3PYdtOFgI/FJFpwXtTw37ooB2FZVdBSVsznn8diz5Zi5/VJyJTojRlurKqHXwPHY5tmINuIWZLf7dCWXk68EBa68AyOk8HXlHVOV7nWN8Q65scvu6lma+zKMuiyJLJatuAdsKchFlEUZntNh07F+kFGhFuhZoaPF9Agc1aAWsiPbO6wjth/6xV2473IrbjIc9mPhiLrj4D49O8RbAsT8Ec4hltNsXalzd+hNviflih3nj5P3dZfgJbHMu2xT1eUi9o7LM/0Gy3vwu5thCqmkUXfgWzGTM5LeKDu4AD3Wl+AjA7Wjgr4oUqyLM9BgJ7YI6ztdj5UgsonoNmY/7umP68XqS27TbeFvdQBT27QaHI05zw4eNmbEJwnar2ZjznA85hwGgRUYyhVUSmtjuhKsEbwFbRs6HYwFuDqt4vIhdRDyfNhap+ICI/wELlMyzAhKQBIjIaG7Du9TZvgkUCXRklnQTsLiJL/PtgbE/+NUGatmno7/Wo6hixM1geEZGjsdWVnURkcBwF4cbGcdjKy8bYnuAPRGRLVX3bk7Wkqao+g60i3+BtnuJ0Gkujxx1VXSki74rIx6NVqLHAg0VtxAaX7JyKEFX6fLLT8zIsMqTsrKPbsS05XVg0V4YTvJzF3h+DsUnwN0Xknag9feWRUrTgg2cxWv4yeGUs0TkJJVjdwpDulN5HYvz1jLd9M8zxcWerdhH0fcjbqpq3WpjhWaI+8MF6W8yJukOFdmRY7fV6GQsvXoiF+m6Kraxug0UdLcAmvqOAo4P3C2XeVwtnYeH+y4N3ejC5DWURrC/vpBFXYKt+M+MyMTr3BGWuBVDVHhF5FDMkLhWRYRitX3daVeXVLHopDJvOeCSjZUjXTC885eXU+tzrei7wnvNyLxZu/uugTQcFdBzm7y4A9haRgTnRS0X8uth1USy7VVFVzprkSUQK6xQ+UNVF7oAIz+N5FjPYG7LEDl8N9XtLeesEzjfLMR6f2yJ5Vb2bq1tp3raz2nXA9diBxGtEpIgn7vX69tvY1KKtIZ4FxojIAHeSZmdXjPHfoH19VlZWnp7bCZv09QcWUHyWUr/yWYsxIMM/A7fgfVJBjicB24pItt1nuIjspqqL3PacC8wVkXsxHTqtk7oXILdsCmyEHDS0Ncgz5PktsAng09g2umtz0jTIBbRlB68RkSdpc2zz71PVzlQ7E3PuttqtsIpAN7oOfBMbt7WTPsbGkd4gbaxvBtCsb2K+ztLU+FpV5/o4uUpVF0rTsVa1dCtEZB6wv4i8jNvcIvJNTHcPC8b5uK5l6MXoGdqs52LRSWAO+E9T552hmDwtwM5rWlug637jn1eLyCZaj/Yqso/C8negzk8neDnDsC2ua/yv1r8u71meh2LOp3ux/n4bs7Ueo7XdXgUDsEOt89AwJnu93vHPNVsI44mNMF5Y5MlXYZGIp9JoC+0MbBnMveYAc0TkGUxOx1HAByJyDxYpP5HmiKhOsBzr2xk02x5jsEi2bHtfdgj4hURz0Biq+piPYVvnJqinW996tt+QIpc2UKjqUkxJXxX99GXgBlUdoaojVXVHzNgb34/FL8IGlT0AfKVgb/L3Ql+EnZHRCtdi4cWZ8NwPbCoiX8kSiB2Q92Ps1qWR/jfc6zIiSDcAU7ijs3SYY6dhNauvNPQVrW8A/6i2n3oG8CNfjUFEthaR47FV3ac9n+2wCd/TmFLL2jWMApqKyBYi0hUUPQZY6p8vwVattvX3NhGR0/y3y4Af+8QasQMXD8JWt4rauCP5qNTnrty+jUWi7V6QF5gB9B2flISYhN3okPXbWOp7yC/B9spn21J+j+37b5tHKqKMD6YDU0RkjJc7DFsx7OQg6zx0Su9JwGkB/XYm/+DC0r4PebtFPe8DNhORk72eA7Fbya70FbrHsdWhjD/HYc6i/yrIr1Y3LPz7HSyC7kTMADoDMzL+QW1LDp5vK5n/PvCgRucDqeq7WHj85V53vC2b0TwpfhNbtf2buEzM8I3LHCFmLczBjJx1mEE6BTuMEk/bklfVzmnYymmSYQ6+ncvrflKQ72XA+SLyCf9+POYoGOF1Xor1wXhsgrwHcJXL1nhgp4COZ2AO3h5sJfI73i5EZKSIHKW2aviaiBzmz4diq2jZGU4Nsus67WRao2M5q1CnEBdjE4YMs7BJ4+H+7iCMb+Nyq8hb2xCRbTyvpa3SQmW9W6Zb4/KPAz4L3FjGE+tpbKoEVX0Ri3AMo0K+Bczz38K0VfVZEYr03LU+9vcHfgYcIMFh9SJysFi0R3/zWZUx4HnMqRZur8iVY9czW6jq9kEdL8F4ZLiI7BvkEfJIn1FWNgV2pNg2khritoY8jzlAjsB5Pqt/mVzkVLOqHfwD2h/bQlwJDBCRVlFta7DzADPZHIrpt8OwrVJt9XFBGbG+WUWzvon5ehX5fP0Nmo/OaIC/sw+2yFOzuT3vEVhk2bFleRRgDTbm3Iod3D0Q6/dl/vudwFQfCwdikTO7YX0JpqNiXbcn5swEc0qd5L8Nwvo6G8dDhDbzL4AdROQAnM7Y+HULptdHYFFmWRTdFGyL23FYH1/q9P4PbBv5cCzyqZXdXgrPfyDFZxfNwbbIZYeuT6HuiJqEOUL+GnOWfdLrlR18vg6z1b5I3Rb6LOawuRqYKSKjvB7ZgeW9lPPBjZhT6WOYc62vmIdtwzsEtz1ch2fPznO634JtyTzA2xzPQRvgfTIQP9uwIM161bP9Dt0Arqz7//SHCcPLwd/ZNF+f/OWc95Zg3tAH8OsWg9++ht1A0te6bQS84Z8PxBRTdlXpEUG6OTReLf0kfgUrwZXMRNeUez0VGOnfh2OTuR5sFeAu/z2+Ev5yLOrpcExxHELzVcsDMS/xdn2hIc3XZAvmLBqPRR18D1vJnE89dH0mwfW43q6HsYE0a9duRTTF9nb/ivrVmI9E9D3Fy1vg/88O6naB1+cFbBAb7b8VtfFuouu7g9/b6fNzgBkhXf1z3nXSXdgAPRLbQiTR7/OwsFHBDLQXvJ3/CfxdmzzSha34hjL2aa//8uDZz8v4wD8f7HR43ut0ehuylHvdMo1X8bZL75nYGUWDozxvBSYE3yv1PY283UXz1d3ZdcA7YqtqizDnydVR3sd4H3ZjfL9vLHNZ28O6YUbGTWHdsFW9FdSvj5+CGdRlMr+988RzUf1nebpNsRW7Hm/DHcCOBX3yMUxup4VlZmmCMr+OOcMWelmvUL8uejawtad/iXJevTN4frS3o8u/D8EmpJmz+nsEV5RjRtiT3u53sVD17LfTMX5/y+twa0jzqD41mmMr5tc4reZjfPhJTzfK+y+j7+SIl2LZPamAl0fSyIct5YxieSqr07UE4wAmJ0uC76OpX0n8Is1j8/lUkLdAxxXpnXGBLGRXPy8ATg3eD68T78avPc+hXah3a3SktW6dRuOV1bdRv7K6jCeG0M9jU4nOzLONtgL+HePHHv/80QI+qqTPPO00giunAz13B6YjejCdsWlVnV/SrlC/7I5tj1qEOTtuwiaKlfisjTKrjgF7O92nlMmx9+WlUX57YbpnBObkya62vxfYJU8Gy2Q5pw3TsAl1Ydn+Oc+O3C2HP2ptJeB5bLL+qNf/A2xi/2e01pVzKLCDo3ca6hE8n0Lrsa3JnsUidu4romdAt1GYgykblyY7Ty1pt4+r6Bun7Rrshr6VmD7s9XQvZ3X1Okwgmh8E+dTaS+OV8c9ht6dBZHP7s6OBu/1zF8HYmpNXN/DboE5f9f5/0b+fSH0eMwT4nbfnPe//44I+XOF0ft/bvwIYGpS7PWb/dmP66Zyor3pp1FMjvf4PY/ZhdvHO7dTHknmYs2i5l/lHbJy/DVtU2j1o8zjqNkdst2fjUTdwfYEMZuPGIs//3Yimr3mbu7EdHhcE+c7GDhfPjj5YjEVQH+jvX44taF3gNMpstdcwW+hRTC9vgjmesj5Y5fTJbpot4oONvOyYr+eQzwvTnJa1cSjgkWmYXGU6fClmd72F6Z13cB2O8zDNtvkS6vZwOOY/BRwVyNZqGnnia5To2Q3xT7wxCQnZmSXXqOp+H3Zd8iAiXwe2V9UqK0QJCQn9DF+huRE4Vv2Gr4SEhISEhISE/80QuzBiJrar5yRtc4Isdobebdh5T6WRWAkJ/5eRnEsJAIjIVzHv6N+rX8+8IUFEZmD7cU9Q2+6WkJCQkJCQkJCQkJCQkJCwASA5lxISEhISEhISEhISEhISEhISOkY60DshISEhISEhISEhISEhISEhoWMk51JCQkJCQkJCQkJCQkJCQkJCQsdIzqWEhISEhISEhISEhISEhISEhI6RnEsJCQkJCQkJCQkJCQkJCQkJCR0jOZcSEhISEhISEhISEhISEhISEjpGci4lJCQkJCQkJCQkJCQkJCQkJHSM/wFuRF9f4KMeNwAAAABJRU5ErkJggg==\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "bMXlxM5abxnX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dataset.METODODX.hist()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "WHmn6gFyOO8k",
        "outputId": "be437369-9f09-41a2-cba5-6f63093743ac"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7ff72658b490>"
            ]
          },
          "metadata": {},
          "execution_count": 8
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dataset.groupby('PROVINCIA').size().plot()"
      ],
      "metadata": {
        "id": "wVuKRdqlv5bw",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 296
        },
        "outputId": "6d5c19df-fb64-48f9-ed16-94b44946add3"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7ff725ff8910>"
            ]
          },
          "metadata": {},
          "execution_count": 9
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Grafico de resultados de los 3 metodos por año"
      ],
      "metadata": {
        "id": "rhG-2neqc4Di"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df[['FECHA_RESULTADO', 'METODODX']].groupby('FECHA_RESULTADO').count().rolling(window = 1, center =False).mean().plot()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "vTifWlpBbEbL",
        "outputId": "cf003e87-9f69-4a81-d346-d7fd032dc80a"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7ff725f8e850>"
            ]
          },
          "metadata": {},
          "execution_count": 10
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "\n",
        "A= df[['METODODX', 'SEXO']].groupby('METODODX').count().rename(columns = {'SEXO': 'count'})\n",
        "\n",
        "A"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 175
        },
        "id": "7FUxO5knyTpM",
        "outputId": "7983f1ab-9970-46b3-8a09-f311fec6c544"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "           count\n",
              "METODODX        \n",
              "AG        468796\n",
              "PCR       311166\n",
              "PR        268613"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3a946f6d-f13d-4de4-95d5-a8bec4566de3\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>METODODX</th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>AG</th>\n",
              "      <td>468796</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PCR</th>\n",
              "      <td>311166</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PR</th>\n",
              "      <td>268613</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3a946f6d-f13d-4de4-95d5-a8bec4566de3')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-3a946f6d-f13d-4de4-95d5-a8bec4566de3 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-3a946f6d-f13d-4de4-95d5-a8bec4566de3');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "count = [468796,311166,268613]\n",
        "nombres = [\"AG\",\"PCR\",\"PR\"]\n",
        "plt.pie(count, labels=nombres, autopct=\"%0.1f %%\")\n",
        "plt.axis(\"equal\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 249
        },
        "id": "Ih-rAr-6y50s",
        "outputId": "cbdbca66-5201-428f-bf17-61ad9d716501"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "RVkWuNMwIdUF"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}