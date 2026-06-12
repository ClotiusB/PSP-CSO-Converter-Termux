# PSP-CSO-Converter-Termux

Converta jogos PSP ISO para CSO diretamente no Android usando Termux.

## Recursos

- Conversão em lote de ISO → CSO
- Nível de compressão fixo em 9 (compressão máxima)
- Suporte para idiomas Português e Inglês
- Relatório detalhado de compressão
- Opção de manter ou remover arquivos ISO originais
- Criação automática de pastas PSP-Iso e PSP-Cso
- Saída direta para pasta de destino
- Interface de terminal limpa

## Requisitos

- Dispositivo Android
- Termux
- Permissão de armazenamento concedida
- Pacote ciso instalado
- Pacote git instalado

## Instalação

**Atualize os pacotes do Termux:**

```bash
pkg update -y
pkg upgrade -y
```

**Instale os pacotes necessários:**

```bash
pkg install python -y
pkg install ciso -y
pkg install git -y
```

**Conceda acesso ao armazenamento:**

```bash
termux-setup-storage
```

**Clone este repositório:**

```bash
git clone https://github.com/SEU_USUARIO/PSP-CSO-Converter-Termux.git
```

**Entre no diretório do projeto:**

```bash
cd PSP-CSO-Converter-Termux
```

**Execute o script:**

```bash
python compress_psp_isos.py
```

## Estrutura de Pastas

O script cria automaticamente:

- `/sdcard/Download/PSP-Iso`
- `/sdcard/Download/PSP-Cso`

Coloque seus arquivos PSP ISO dentro de:

```
/sdcard/Download/PSP-Iso
```

**Exemplo:**

```
PSP-Iso
├── God of War - Chains of Olympus.iso
├── Tekken 6.iso
├── GTA Vice City Stories.iso
```

Os jogos compactados serão salvos em:

```
/sdcard/Download/PSP-Cso
```

**Exemplo:**

```
PSP-Cso
├── God of War - Chains of Olympus.cso
├── Tekken 6.cso
├── GTA Vice City Stories.cso
```

## Uso

1. Inicie o script
2. Selecione seu idioma
3. Escolha se deseja manter ou remover os arquivos ISO após compressão
4. Aguarde a conversão terminar
5. Revise o relatório final de compressão

**Exemplo de Saída:**

```
==================================================
INICIANDO COMPRESSÃO
==================================================

==================================================
[1/3] Processando: Tekken 6.iso
==================================================

Conversão concluída

==================================================
[2/3] Processando: God of War - Chains of Olympus.iso
==================================================

Conversão concluída
```

## Informações de Compressão

Este projeto usa:

```bash
ciso 9 input.iso output.cso
```

**Nível de compressão:**

- `9` = Compressão Máxima

## Notas

- Arquivos CSO existentes são pulados automaticamente
- Arquivos ISO podem ser mantidos ou removidos após a conversão
- O script gera arquivos CSO diretamente no diretório de saída
- Suporta todos os jogos PSP armazenados como imagens ISO

## Licença

[MIT License](https://github.com/ClotiusB/PSP-CSO-Converter-Termux#)

