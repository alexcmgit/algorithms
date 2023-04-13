<p><a href="https://www.beecrowd.com.br/repository/UOJ_2607_en.html">beecrowd.com.br/repository/UOJ_2607_en.html</a></p><hr>
                          <div>
                            <span>URI Online <strong>SQL</strong> | 2607 </span>
                            <h1>Providers' City in Alphabetical Order</h1>
                            <div>
                              <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
                            </div>
                            <strong>Timelimit: 1</strong>
                          </div>
                          <div>
                          <div>
                            <p>Every month the company asks for a report from the cities that providers are registered. So, do a query that returns all the cities of the providers, but in alphabetical order.</p>
                            <p>OBS: You must not show repeated cities.</p>
                          </div>
                          <div>
                          <h2>Schema</h2>
                          <div>
                          <table>
                          <caption>providers</caption>
                          <tbody><tr>
                          <td><strong>Column</strong></td>
                          <td><strong>Type</strong></td>
                        </tr>
                        <tr>
                          <td>id (PK)</td>
                          <td>numeric</td>
                        </tr>
                        <tr>
                          <td>name</td>
                          <td>varchar</td>
                        </tr>
                        <tr>
                          <td>street</td>
                          <td>varchar</td>
                        </tr>
                        <tr>
                          <td>city</td>
                          <td>varchar</td>
                        </tr>
                        <tr>
                          <td>state</td>
                          <td>char</td>
                        </tr>
                      </tbody></table>
                    </div>
                  </div>
                  <div>
                  <h2>Tables</h2>
                  <div>
                  <table>
                  <caption>providers</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                  <td><strong>street</strong></td>
                  <td><strong>city</strong></td>
                  <td><strong>state</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>Henrique</td>
                  <td>Av Brasil</td>
                  <td>Rio de Janeiro</td>
                  <td>RJ</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Marcelo Augusto</td>
                  <td>Rua Imigrantes</td>
                  <td>Belo Horizonte</td>
                  <td>MG</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Caroline Silva</td>
                  <td>Av São Paulo</td>
                  <td>Salvador</td>
                  <td>BA</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>Guilerme Staff</td>
                  <td>Rua Central</td>
                  <td>Porto Alegre</td>
                  <td>RS</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>Isabela Moraes</td>
                  <td>Av Juiz Grande</td>
                  <td>Curitiba</td>
                  <td>PR</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>Francisco Accerr</td>
                  <td>Av Paulista</td>
                  <td>São Paulo</td>
                  <td>SP</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>city</strong></td>
        </tr>
        <tr>
          <td>Belo Horizonte</td>
        </tr>
        <tr>
          <td>Curitiba</td>
        </tr>
        <tr>
          <td>Porto Alegre</td>
        </tr>
        <tr>
          <td>Rio de Janeiro</td>
        </tr>
        <tr>
          <td>Salvador</td>
        </tr>
        <tr>
          <td>São Paulo</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>